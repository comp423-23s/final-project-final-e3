from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from .entity_base import EntityBase
from ..models import Reservation
from . import RoomEntity

class ReservationEntity(EntityBase):
    __tablename__ = 'reservation'

    identifier_id: Mapped[str] = mapped_column(String, primary_key=True)
    subject_name: Mapped[str] = mapped_column(String)
    pid: Mapped[int] = mapped_column(Integer)
    start: Mapped[str] = mapped_column(String)
    end: Mapped[str] = mapped_column(String)

    @classmethod
    def from_model(cls, model: Reservation) -> Self:
        return cls(
            identifier_id=model.identifier_id,
            subject_name=model.subject_name,
            pid=model.pid,
            start=model.start,
            end=model.end,
        )

    def to_model(self) -> Reservation:
        return Reservation(
            identifier_id=self.identifier_id,
            subject_name=self.subject_name,
            pid=self.pid,
            start=self.start,
            end=self.end,
        )