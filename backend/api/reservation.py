from fastapi import APIRouter, Depends
from ..services import ReservationService
from ..models import ReservationRequest, Reservation

"""
POST for a new reservation:
"/api/reserve/room/{Room_name}", payload=Reservation
"""

api = APIRouter(prefix="/api/reserve")

@api.post("/room/{name}")
def new_reservation(reservation: Reservation, room_name: str, reservation_svc: ReservationService = Depends()) -> str:
    """Creates a new reservation for a specific room_name."""
    pass

