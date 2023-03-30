from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import ReservationRequest, Reservation
from ..entities import ReservationEntity


class ReservationService:

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def list(self, room_name: str) -> list[str]:
        """Lists all reservations for a room."""
        pass

    def add(self, reserv_request: ReservationRequest, room_name: str) -> None:
        """Add reservation to database. """
        pass

    def remove(self, reservation_id: str, id: int, userId: int):
        """Remove reservation"""
        pass