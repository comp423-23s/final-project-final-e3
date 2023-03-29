from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from .entity_base import EntityBase
from ..models import Equipment


class EquipmentEntity(EntityBase):
    __tablename__ = "equipment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    max_capacity: Mapped[int] = mapped_column(Integer)
    reservations: Mapped[list['ReservationEntity']] = relationship(back_populates='equipment')

    @classmethod
    def from_model(cls, model: Equipment) -> Self:
        return cls(
            id=model.id,
            name=model.name
        )

    def to_model(self) -> Equipment:
        return Equipment(
            id=self.id,
            name=self.name
        )