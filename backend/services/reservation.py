from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session, joinedload
from ..database import db_session
from ..models import Reservation
from ..entities import RoomEntity, ReservationEntity, UserEntity, RoleEntity


class ReservationService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

        
    def list(self, subject_name_or_pid: str | int) -> list[Reservation] | None:
        """Lists all reservations for a room."""
        is_PID = subject_name_or_pid.isdigit()

        statement = select(ReservationEntity)
        reservation_entities = self._session.execute(statement).scalars()
        if not is_PID:
            return [reservation_entity.to_model() for reservation_entity in reservation_entities if reservation_entity.subject_name == subject_name_or_pid]
        
        return [reservation_entity.to_model() for reservation_entity in reservation_entities if reservation_entity.pid == int(subject_name_or_pid)] 


    def list_all(self):
        """Only staff can list all reservations in database."""
        statement = select(ReservationEntity)
        reservation_entities = self._session.execute(statement).scalars()
        return [reservation_entity.to_model() for reservation_entity in reservation_entities] 


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