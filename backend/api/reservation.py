from fastapi import APIRouter, Depends
from ..models import Reservation
from ..services import ReservationService

api = APIRouter(prefix="/api/reserve")

@api.get("", response_model=list[Reservation], tags=['Reservation'])
def list_all(reserve_svc: ReservationService = Depends()):
    return reserve_svc.list_all(user_pid)

@api.get("/{subject_name_or_pid}", response_model=list[Reservation], tags=['Reservation'])
def list(subject_name_or_pid: str | int, reserve_svc: ReservationService = Depends()):
    return reserve_svc.list(subject_name_or_pid)

@api.post("", tags=['Reservation'])
def add(reservation: Reservation, reserve_svc: ReservationService = Depends()) -> None:
    return reserve_svc.add(reservation)

@api.delete("", tags=['Reservation'])
def delete(reservation_id: str, reserve_svc: ReservationService = Depends()) -> None:
    return reserve_svc.delete(reservation_id)