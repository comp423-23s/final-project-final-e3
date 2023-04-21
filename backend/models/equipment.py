"""Equipment model representing reservable equipments"""

from pydantic import BaseModel
from typing import Dict, List

class Equipment(BaseModel):
    name: str
    availability: Dict[str,List[str]]