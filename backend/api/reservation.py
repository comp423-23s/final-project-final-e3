from fastapi import APIRouter
from ..models import Reservation, ReservationRequest

"""
POST for a new reservation:
"/reserve/room/name=<Room_name>", payload=Reservation
"""

api = APIRouter(prefix="/api/reserve")

@api.post("/room/{name}")
def new_reservation(request: ReservationRequest) -> Reservation:
    pass

