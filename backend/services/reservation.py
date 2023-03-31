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
        query = select(RoomEntity).where(name == room_name)
        room_entity: RoomEntity =  self._session.scalar(query)
        if room_entity is None:
            return None
        else:
            reservation_entities = room_entity.reservations
            return [reservation_entity.to_model() for reservation_entity in reservation_entities]
        

    def add(self, reservation: Reservation, room_name: str) -> None:
        """Add reservation to database. """
        query = select(RoomEntity).where(name == room_name)
        room_entity: RoomEntity = self._session.scalar(query)
        reservation_entity = reservation.from_model()
        if room_entity is not None:
            reservation_entity.subject = room_entity
            self._session.add(reservation_entity)
            self._session.commit()


    def remove(self, reservation_id: str, id: int, userId: int):
        """Remove reservation"""
        pass