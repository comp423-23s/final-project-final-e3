from fastapi import Depends
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from ..database import db_session
from ..models import Room, User
from ..entities import RoomEntity, UserEntity, RoleEntity
from .permission import PermissionService

class RoomService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session


    def list(self) -> list[Room]:
        """List all rooms"""
        statement = select(RoomEntity).order_by(RoomEntity.name)
        room_entities = self._session.execute(statement).scalars()
        return [room_entity.to_model() for room_entity in room_entities]


    def add(self, user_pid: int, room: Room) -> str:
        """Staff adds a new room into database"""
        staff_entity = self._session.query(UserEntity).filter_by(pid=user_pid).one()
        if staff_entity is None:
            return "User not found"
        role_entities = staff_entity.roles
        roles = [role_entity.to_model() for role_entity in role_entities]
        for role in roles:
            if role.name == "Staff":
                room_entity = RoomEntity.from_model(room)
                self._session.add(room_entity)
                self._session.commit()
                return "room added successfully"
        return "You cannot add rooms"

    def delete(self, user_pid: int, room_name: str) -> str:
        """Staff deletes a room specified by name from database"""
        staff_entity = self._session.query(UserEntity).filter_by(pid=user_pid).one()
        if staff_entity is None:
            return "User not found"
        role_entities = staff_entity.roles
        roles = [role_entity.to_model() for role_entity in role_entities]
        for role in roles:
            if role.name == "Staff":
                room_to_delete = self._session.query(RoomEntity).filter_by(name=room_name).one()
                self._session.delete(room_to_delete)
                self._session.commit()
                return "Room deleted successfully"
        return "You cannot delete rooms"