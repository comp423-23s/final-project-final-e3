"""Room model serves as data object representing reservable rooms"""

from pydantic import BaseModel

class Room(BaseModel):
    id: int | None = None
    name: str
    max_capacity: int
    reservations: list[Reservation]