"""Room services managing and changing rooms and their availability schedules"""

from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Room, User
from ..entities import RoomEntity, UserEntity, RoleEntity
from .permission import PermissionService
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
        self._session.add(room_entity)
        self._session.commit()
        return "room added successfully"


    def delete(self, user_pid: int, room_name: str) -> None:
        """Staff could delete a room specified by name from database"""
        staff_entity = self._session.query(UserEntity).filter_by(pid=user_pid).one()
        staff = staff_entity.to_model()
        self._permission.enforce(staff, 'room.delete', 'room/')
        room_to_delete = self._session.query(RoomEntity).filter_by(name=room_name).one()
        if room_to_delete is None:
            return "Room not found"
        self._session.delete(room_to_delete)
        self._session.commit()