from fastapi import APIRouter, Depends
from ..models import Room
from ..services import RoomService

"""
GET to list all rooms:
"/api/rooms"

GET to list reservations for a room given room_name
"/api/room/{room_name}"
"""

api = APIRouter(prefix="/api/room")

@api.get("", response_model=list[Room], tags=['Room'])
def list_room(room_svc: RoomService = Depends()):
    return room_svc.list()