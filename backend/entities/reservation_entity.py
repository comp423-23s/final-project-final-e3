from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from .entity_base import EntityBase
from ..models import Reservation


class ReservationEntity(EntityBase):
    __tablename__ = "reservation"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    start: Mapped[str] = mapped_column(String)
    end: Mapped[str] = mapped_column(String)
    length: Mapped[int] = mapped_column(Integer)

    subject: Mapped['RoomEntity'] = relationship(back_populates='reservation')
    user: Mapped['UserEntity'] = relationship(back_populates='reservation')

    @classmethod
    def from_model(cls, model: Reservation) -> Self:
        return cls(
            id=model.id,
            start=model.start,
            end=model.end,
            length=model.length
        )

    def to_model(self) -> Reservation:
        return Reservation(
            id=self.id,
            start=self.start,
            end=self.end,
            length=self.length
        )