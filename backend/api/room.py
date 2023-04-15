from fastapi import APIRouter, Depends
from ..models import Room, User
from ..services import RoomService

api = APIRouter(prefix="/api/room")


@api.get("", response_model=list[Room], tags=["Room"])
def list(room_svc: RoomService = Depends()):
    return room_svc.list()

@api.post("", tags=["Room"])
def add(user_pid: int, room: Room, room_svc: RoomService = Depends()) -> None:
    return room_svc.add(user_pid, room)

@api.delete("/{room_name}", tags=["Room"])
def delete(user_pid: int, room_name: str, room_svc: RoomService = Depends()) -> None:
    return room_svc.delete(user_pid, room_name)