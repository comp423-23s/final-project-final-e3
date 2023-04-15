from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Room, User
from ..entities import RoomEntity, UserEntity, RoleEntity
from datetime import datetime, timedelta

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dow_mapping = {}

for idx,day in enumerate(days_of_week):
    dow_mapping[idx] = day
    dow_mapping[day] = idx


def get_sunday_of_week() -> datetime:
    today = datetime.today()
    sunday = today - timedelta(days=(today.weekday()+1))
    return sunday

def get_saturday_of_next_week(weeks_advance: int = 1) -> datetime:
    today = datetime.today()
    days_until_sat = 5 - today.weekday()
    next_week_sat = today + timedelta(days=days_until_sat + 7*weeks_advance)
    return next_week_sat

def list_dates_in_between(start: datetime, end: datetime) -> list[datetime]:
    """Returns list of dates between start and end."""
    dates = []
    while start <= end:
        dates.append(start)
        start += timedelta(days=1)
    return dates

def list_time_slots(start: datetime, end: datetime ,interval: float) -> list[tuple[str]]:
    "Creats a list of time slots."
    slots = []
    while start < end: 
        slot_start = start
        slot_end = slot_start + timedelta(hours=interval)
        slots.append((slot_start.strftime("%H:%M"), slot_end.strftime("%H:%M")))
        start = slot_end
    return slots


class RoomService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session


    def list(self) -> list[Room]:
        """List all rooms"""
        statement = select(RoomEntity).order_by(RoomEntity.name)
        room_entities = self._session.execute(statement).scalars()
        return [room_entity.to_model() for room_entity in room_entities]
    
    def list_schedule(self, room_id:str):
        """Returns list of all available times slots for the next two weeks."""

        room_entity = self._session.query(RoomEntity).filter_by(name=room_id).one()
        room = room_entity.to_model()

        schedule = {}

        this_sun = get_sunday_of_week()
        next_sat = get_saturday_of_next_week()
        dates = list_dates_in_between(this_sun, next_sat)
        for date in dates: 
            start, end, interval = room.availability[dow_mapping[date.weekday()]]
            start = datetime.strptime(start, "%H:%M")
            end = datetime.strptime(end, "%H:%M")
            interval = float(interval)

            try:
                deviations = room.deviations[date.strftime(r"%m/%d")]
            except KeyError:
                deviations = []

            if deviations:
                time_slots = deviations
            else:
                time_slots = list_time_slots(start, end, interval)

            schedule[date.strftime(r"%m/%d")] = time_slots
                
        return schedule
    
    def edit_schedule(self, room_name, deviations) -> None:
        room_entity = self._session.query(RoomEntity).filter_by(name=room_name).one()
        room = room_entity.to_model()

        # Does not change room's schedule, but does change rooms deviations list. 
        for date_str in deviations:
            room.deviations[date_str] = deviations[date_str]

        self.delete(room.name)
        self.add(room)


    def add(self, user_pid: int, room: Room) -> str:
        """Staff adds a new room into database"""
        staff_entity = self._session.query(UserEntity).filter_by(pid=user_pid).one()
        if staff_entity is None:
            return "User not found"
        role_entities = staff_entity.roles
        roles = [role_entity.to_model() for role_entity in role_entities]
        for role in roles:
            if role.name == "Staff":
                room_entity = RoomEntity.from_model(room)
                self._session.add(room_entity)
                self._session.commit()
                return "room added successfully"
        return "You cannot add rooms"

    def delete(self, user_pid: int, room_name: str) -> str:
        """Staff deletes a room specified by name from database"""
        staff_entity = self._session.query(UserEntity).filter_by(pid=user_pid).one()
        if staff_entity is None:
            return "User not found"
        role_entities = staff_entity.roles
        roles = [role_entity.to_model() for role_entity in role_entities]
        for role in roles:
            if role.name == "Staff":
                room_to_delete = self._session.query(RoomEntity).filter_by(name=room_name).one()
                self._session.delete(room_to_delete)
                self._session.commit()
                return "Room deleted successfully"
        return "You cannot delete rooms"