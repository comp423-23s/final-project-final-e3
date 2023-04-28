"""Equipment model representing reservable equipment"""

from pydantic import BaseModel
from typing import Dict, List

class Equipment(BaseModel):
    name: str
    availability: Dict[str,List[str]]
    deviations: Dict[str, List[str]]