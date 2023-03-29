"""Equipment model representing reservable equipments"""

from pydantic import BaseModel

class Equipment(BaseModel):
    id: int | None = None
    name: str
    reservations: list[Reservation]