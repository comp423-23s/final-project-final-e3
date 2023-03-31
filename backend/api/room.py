from fastapi import APIRouter, Depends
from ..models import Room
from ..services import RoomService

api = APIRouter(prefix="/api/room")


@api.get("", response_model=list[Room], tags=['Room'])
def list(room_svc: RoomService = Depends()):
    return room_svc.list()


@api.post("", tags=['Room'])
def add(id: int, name: str, max_capacity: int, room_svc: RoomService = Depends()) -> None:
    return room_svc.add(id, name, max_capacity)