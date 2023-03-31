"""Reservation model representing reservation required by users"""

from pydantic import BaseModel
from datetime import datetime

class Reservation(BaseModel):
    id: int | None = None
    room_name: str
    user_pid: int
    start: datetime
    end: datetime
    length: int