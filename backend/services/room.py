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
        statement = select(RoomEntity).order_by(RoomEntity.name)
        room_entities = self._session.execute(statement).scalars()
        return [room_entity.to_model() for room_entity in room_entities]


    def add(self, room: Room) -> None:
        """Add room into database"""
        room_entity = RoomEntity.from_model(room)
        self._session.add(room_entity)
        self._session.commit()


    def delete(self, room_name: str) -> None:
        """Delete a room specified by name from database"""
        room_to_delete = self._session.query(RoomEntity).filter_by(name=room_name).one()
        self._session.delete(room_to_delete)