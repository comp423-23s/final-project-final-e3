from fastapi import APIRouter, Depends
from ..models import Room, User
from ..services import RoomService
from typing import List, Dict, Tuple

api = APIRouter(prefix="/api/room")


@api.get("", response_model=list[Room], tags=["Room"])
def list(room_svc: RoomService = Depends()):
    return room_svc.list()

@api.get("/{room_name}", tags=["Room"])
def list_schedule(room_name: str, room_svc: RoomService = Depends()):
    return room_svc.list_schedule(room_name)

@api.post("/edit/{room_name}", tags=["Room"])
def edit_schedule(room_name: str, deviations: Dict[str,List[Tuple[str, str]]], room_svc: RoomService = Depends()):
    return room_svc.edit_schedule(room_name, deviations)

@api.post("", tags=["Room"])
def add(user_pid: int, room: Room, room_svc: RoomService = Depends()) -> None:
    return room_svc.add(user_pid, room)

@api.delete("/{room_name}", tags=["Room"])
def delete(user_pid: int, room_name: str, room_svc: RoomService = Depends()) -> None:
    return room_svc.delete(user_pid, room_name)