"""Room model serves as data object representing reservable rooms"""

from pydantic import BaseModel

class Room(BaseModel):
    id: int
    name: str
    max_capacity: int