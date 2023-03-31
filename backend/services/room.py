from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Room
from ..entities import RoomEntity

class RoomService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def list(self) -> list[Room]:
        """List all rooms"""
        statement = select(RoomEntity)
        room_entities = self._session.execute(statement).scalar()
        return [room_entity.to_model() for room_entity in room_entities]