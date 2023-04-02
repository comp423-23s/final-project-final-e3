"""Reservation model representing reservation required by users"""

from pydantic import BaseModel

class Reservation(BaseModel):
    id: int
    pid: int
    subject_name: str
    start: str
    end: str
