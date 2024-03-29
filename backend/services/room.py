"""Room services managing and changing rooms and their availability schedules"""

import json
from fastapi import Depends
from sqlalchemy import select, or_, func, update
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Room, User
from ..entities import RoomEntity, UserEntity, RoleEntity, ReservationEntity
from .permission import PermissionService
from .reservation import ReservationService
from datetime import datetime, timedelta
from sqlalchemy import exc
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
    _permission: PermissionService

    def __init__(self, session: Session = Depends(db_session), permission: PermissionService = Depends()):
        self._session = session
        self._permission = permission


    def list(self) -> list[Room]:
        """List all rooms"""
        statement = select(RoomEntity).order_by(RoomEntity.name)
        room_entities = self._session.execute(statement).scalars()
        return [room_entity.to_model() for room_entity in room_entities]


    def add(self, user_pid: int, room: Room) -> None:
        """Staff could add a new room into database"""
        staff_entity = self._session.query(UserEntity).filter_by(pid=user_pid).one()
        staff = staff_entity.to_model()
        self._permission.enforce(staff, 'room.add', 'room/')

        room_entity = RoomEntity.from_model(room)
        try: 
            self._session.add(room_entity)
            self._session.commit()
        except exc.SQLAlchemyError:
            raise Exception("The room has already been added.");
        return


    def delete(self, user_pid: int, room_name: str) -> None:
        """Staff could delete a room specified by name from database"""
        staff_entity = self._session.query(UserEntity).filter_by(pid=user_pid).one()
        staff = staff_entity.to_model()
        self._permission.enforce(staff, 'room.delete', 'room/')

        # Delete room
        room_to_delete = self._session.query(RoomEntity).filter_by(name=room_name).one()
        if room_to_delete is None:
            return "Room not found"
        self._session.delete(room_to_delete)

        # Delete all reservations associated with room
        statement = select(ReservationEntity)
        reservation_entities = self._session.execute(statement).scalars()
        room_reservations_ids = [reservation_entity.to_model().identifier_id for reservation_entity in reservation_entities if reservation_entity.subject_name==room_name]
        for id in room_reservations_ids:
            reservation_to_delete = self._session.query(ReservationEntity).filter_by(identifier_id=id).one()
            self._session.delete(reservation_to_delete)
        self._session.commit()
        return
        
        
    def edit_deviations(self, user_pid, room_name, deviations) -> None:
        staff_entity = self._session.query(UserEntity).filter_by(pid=user_pid).one()
        staff = staff_entity.to_model()
        self._permission.enforce(staff, 'room.delete', 'room/')

        room_entity = self._session.query(RoomEntity).filter_by(name=room_name).one()
        room = room_entity.to_model()

        # Does not change room's schedule, but does change rooms deviations list. 
        room.deviations.update(deviations)

        #self._session.query(RoomEntity).filter_by(name=room_name).one().update({RoomEntity.deviations:deviations}, synchronize_session=False)
        room_entity.deviations = json.dumps(room.deviations)
        self._session.commit()
        return
    

    def remove_expired_deviations(self, room_name, deviations, dates):
        """Removes expired entries from a deviations dictionary. Returns new deviations dict."""
        dates = [date.strftime(r"%m/%d") for date in dates]
        to_delete_dates = []
        for date_str in deviations:
            if date_str not in dates:
                to_delete_dates.append(date_str)
       
        if len(to_delete_dates) == 0:
            return deviations
        else:
            for date in to_delete_dates:
                del deviations[date]
        
        # Same functionality as edit, bypass PID check since internal function.  
        room_entity = self._session.query(RoomEntity).filter_by(name=room_name).one()
        room = room_entity.to_model()
        room.deviations = deviations

        # Update database
        #self._session.query(RoomEntity).filter_by(name=room_name).one().update({RoomEntity.deviations:deviations}, synchronize_session=False)
        room_entity.deviations = json.dumps(deviations)
        self._session.commit()
        return deviations
    

    def list_schedule(self, room_id:str):
        """Returns list of all available times slots for the next two weeks."""

        room_entity = self._session.query(RoomEntity).filter_by(name=room_id).one()
        room = room_entity.to_model()

        # Get all reserved slots for room
        statement = select(ReservationEntity)
        reservation_entities = self._session.execute(statement).scalars()
        room_reservations = [reservation_entity.to_model() for reservation_entity in reservation_entities if reservation_entity.subject_name==room_id]

        reservations = {}
        for reservation in room_reservations:
            start_time, start_date = reservation.start.split("-")
            if start_date in reservations:
                reservations[start_date].append(start_time)
            else:
                reservations[start_date] = [start_time]

        schedule = {}

        this_sun = get_sunday_of_week()
        next_sat = get_saturday_of_next_week()
        dates = list_dates_in_between(this_sun, next_sat)

        # Remove expired deviations
        deviations = room.deviations
        deviations = self.remove_expired_deviations(room_id, deviations, dates)

        # Generate time slots according to original schedule
        for date in dates: 
            try:
                start, end, interval = room.deviations[date.strftime(r"%m/%d")]
            except KeyError:
                start, end, interval = room.availability[dow_mapping[date.weekday()]]
            
            start = datetime.strptime(start, "%H:%M")
            end = datetime.strptime(end, "%H:%M")
            interval = float(interval)

            time_slots = list_time_slots(start, end, interval)

            # Check if slot has been reserved
            date_str = date.strftime(r"%m/%d")
            try:
                assert date_str in reservations
                for slot in time_slots:
                    slot_start = slot[0]
                    if not slot_start in reservations[date_str]:
                        if date_str in schedule:
                            schedule[date_str].append(slot)
                        else:
                            schedule[date_str] = [slot]
            except AssertionError: # No reservations for date
                schedule[date_str] = time_slots       
        return schedule
