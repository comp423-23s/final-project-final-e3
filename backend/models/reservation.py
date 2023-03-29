"""Reservation model representing reservation required by users"""

from pydantic import BaseModel
from datetime import datetime
from . import Room, Equipment, User

class Reservation(BaseModel):
    id: int | None = None
    subject: Room | Equipment
    user: User
    start: datetime
    end: datetime
    length: int