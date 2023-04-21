from sqlalchemy import Integer, String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from typing import Self
from .entity_base import EntityBase
from ..models import Equipment
import json

class EquipmentEntity(EntityBase):
    __tablename__ = "equipment"

    name: Mapped[str] = mapped_column(String, primary_key=True)
    availability: Mapped[dict[str:list[str]]] = mapped_column(JSON)

    @classmethod
    def from_model(cls, model: Equipment) -> Self:
        return cls(
            name=model.name,
            availability=json.dumps(model.availability)
        )

    def to_model(self) -> Equipment:
        return Equipment(
            name=self.name,
            availability=json.loads(self.availability)
        )