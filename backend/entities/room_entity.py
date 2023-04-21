from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON
from typing import Self
from .entity_base import EntityBase
from ..models import Room
import json

class RoomEntity(EntityBase):
    __tablename__ = 'room'

    name: Mapped[str] = mapped_column(String, primary_key=True)
    max_capacity: Mapped[int] = mapped_column(Integer)
    availability: Mapped[dict[str:list[str]]] = mapped_column(JSON)
    deviations: Mapped[dict[str,list[tuple[str, str]]]] = mapped_column(JSON)

    @classmethod
    def from_model(cls, model: Room) -> Self:
        return cls(
            name=model.name,
            max_capacity=model.max_capacity,
            availability=json.dumps(model.availability),
            deviations=json.dumps(model.deviations)
        )

    def to_model(self) -> Room:
        return Room(
            name=self.name,
            max_capacity=self.max_capacity,
            availability=json.loads(self.availability),
            deviations=json.loads(self.deviations)
        )