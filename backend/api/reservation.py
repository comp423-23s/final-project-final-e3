from fastapi import APIRouter, Depends
from ..models import Reservation
from ..services import ReservationService

api = APIRouter(prefix="/api/reserve")


@api.get("/{subject_name}", response_model=list[Reservation], tags=['Reservation'])
def list(subject_name: str, reserve_svc: ReservationService = Depends()):
    return reserve_svc.list(subject_name)


@api.post("", tags=['Room'])
def add(id: int, name: str, max_capacity: int, room_svc: ReservationService = Depends()) -> None:
    # TODO 
    return 