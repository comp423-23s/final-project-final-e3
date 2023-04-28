"""Reservation services managing and changing reservations"""

from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session, joinedload
from ..database import db_session
from ..models import Reservation
from ..entities import RoomEntity, ReservationEntity, UserEntity, RoleEntity
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


class ReservationService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def delete_expired_reservations(self, reservations):
        # Delete outdated reservations
        this_sun = get_sunday_of_week()
        next_sat = get_saturday_of_next_week()
        dates = list_dates_in_between(this_sun, next_sat) # List of dates from last Sunday to next Sat
        dates = [date.strftime(r"%m/%d") for date in dates]

        kept_reservations = []

        for reservation in reservations:
            id = reservation.identifier_id
            start = reservation.start.split("-")[1]
            
            if start not in dates:
                self.delete(id)
            else:
                kept_reservations.append(reservation)
        return kept_reservations
    

    def list(self, subject_name_or_pid: str | int) -> list[Reservation] | None:
        """Lists all reservations for a room."""
        is_PID = subject_name_or_pid.isdigit()

        statement = select(ReservationEntity)
        reservation_entities = self._session.execute(statement).scalars()
        if not is_PID:
            reservations = [reservation_entity.to_model() for reservation_entity in reservation_entities if reservation_entity.subject_name == subject_name_or_pid]
        else:
            reservations = [reservation_entity.to_model() for reservation_entity in reservation_entities if reservation_entity.pid == int(subject_name_or_pid)]

        reservations = self.delete_expired_reservations(reservations)
        return reservations


    def list_all(self):
        """Only staff can list all reservations in database."""
        statement = select(ReservationEntity)
        reservation_entities = self._session.execute(statement).scalars()
        reservations = [reservation_entity.to_model() for reservation_entity in reservation_entities] 

        reservations = self.delete_expired_reservations(reservations)
        return reservations


    def add(self, reservation: Reservation) -> None:
        """Add reservation to database. """
        reservation_entity = ReservationEntity.from_model(reservation)
        self._session.add(reservation_entity)
        self._session.commit()


    def delete(self, id: str) -> None:
        """Remove reservation from database"""
        reservation_to_delete = self._session.query(ReservationEntity).filter_by(identifier_id=id).one()
        self._session.delete(reservation_to_delete)
        self._session.commit()