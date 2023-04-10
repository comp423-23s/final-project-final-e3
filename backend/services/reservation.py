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

        
    def list(self, subject_name: str) -> list[Reservation] | None:
        """Lists all reservations for a room."""
        statement = select(ReservationEntity)
        reservation_entities = self._session.execute(statement).scalars()
        return [reservation_entity.to_model() for reservation_entity in reservation_entities if reservation_entity.subject_name == subject_name]
        

    def add(self, reservation: Reservation) -> None:
        """Add reservation to database. """
        reservation_entity = reservation.to_model()
        self._session.add(reservation_entity)
        self._session.commit()


    def delete(self, user_pid: int, name: str) -> None:
        """Remove reservation from database"""
        entities = self._session.query(ReservationEntity).filter_by(pid=user_pid, subject_name=name).all()
        self._session.delete(entities)
        self._session.commit()