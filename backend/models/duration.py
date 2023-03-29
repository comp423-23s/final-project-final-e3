"""Duration model representing a period of time"""

from pydantic import BaseModel
from datetime import datetime

class Duration(BaseModel):
    start: datetime
    end: datetime
    length: int