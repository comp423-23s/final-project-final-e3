"""Reservation model representing reservation required by users"""

from pydantic import BaseModel

class Reservation(BaseModel):
    identifier_id: str
    pid: int
    subject_name: str
    start: str
    end: str