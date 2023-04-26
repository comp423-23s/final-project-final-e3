from fastapi import APIRouter, Depends, HTTPException
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
def edit_deviations(room_name: str, deviations: Dict[str, List[str]], room_svc: RoomService = Depends()):
    return room_svc.edit_deviations(room_name, deviations)

@api.post("", tags=["Room"])
def add(room: Room, room_svc: RoomService = Depends()) -> None:
    try:
        return room_svc.add(room)
    except AssertionError:
        raise HTTPException(status_code=400, detail="Bad room information")

@api.delete("/{room_name}", tags=["Room"])
def delete(room_name: str, room_svc: RoomService = Depends()) -> None:
    return room_svc.delete(room_name)