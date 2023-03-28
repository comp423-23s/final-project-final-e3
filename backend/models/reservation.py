"""Reservation model representing reservation required by users"""

from pydantic import BaseModel

class Reservation(BaseModel):
    subject: Room | Equipment
    user: User
    duration: Duration