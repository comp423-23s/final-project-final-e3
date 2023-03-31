from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session, joinedload
from ..database import db_session
from ..models import Reservation
from ..entities import RoomEntity, ReservationEntity


class ReservationService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session


    def list(self, room_name: str) -> list[Reservation] | None:
        """Lists all reservations for a room."""
        statement = select(ReservationEntity)
        reservation_entities = self._session.execute(statement).scalars()
        return [reservation_entity.to_model() for reservation_entity in reservation_entities 
                if reservation_entity.subject_name == room_name]
        

    def add(self, reservation: Reservation, room_name: str) -> None:
        """Add reservation to database. """
        pass


    def remove(self, reservation_id: str, id: int, userId: int):
        """Remove reservation"""
        pass