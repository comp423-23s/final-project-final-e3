from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Self
from .entity_base import EntityBase
from ..models import Room

class RoomEntity(EntityBase):
    __tablename__ = 'room'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    max_capacity: Mapped[int] = mapped_column(Integer)

    @classmethod
    def from_model(cls, model: Room) -> Self:
        return cls(
            id=model.id,
            name=model.name,
            max_capacity=model.max_capacity,
        )

    def to_model(self) -> Room:
        return Room(
            id=self.id,
            name=self.name,
            max_capacity=self.max_capacity,
        )