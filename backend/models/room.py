"""Room model serves as data object representing reservable rooms"""

from pydantic import BaseModel
from typing import Dict, List, Tuple

class Room(BaseModel):
    name: str
    max_capacity: int
    availability: Dict[str,List[str]]
    deviations: Dict[str, List[str]]