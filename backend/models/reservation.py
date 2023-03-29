"""Reservation model representing reservation required by users"""

from pydantic import BaseModel
from datetime import datetime
from . import Room, Equipment, User

class ReservationRequest(BaseModel):
    pid: int
    start: str
    end: str
    subject_name: str

class Reservation(BaseModel):
    id: int | None = None
    subject: Room | Equipment
    user: User
    start: datetime
    end: datetime
    length: int