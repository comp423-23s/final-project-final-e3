from fastapi import APIRouter, Depends
from ..models import Room
from ..services import RoomService

api = APIRouter(prefix="/api/room")


@api.get("", response_model=list[Room], tags=['Room'])
def list(room_svc: RoomService = Depends()):
    return room_svc.list()


@api.post("", tags=['Room'])
def add(room: Room, room_svc: RoomService = Depends()) -> None:
    return room_svc.add(room)

@api.delete("/{room_name}", tags=["Room"])
def delete(room_name: str, room_svc: RoomService = Depends()) -> None:
    return room_svc.delete(room_name)