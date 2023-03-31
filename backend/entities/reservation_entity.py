from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self
from .entity_base import EntityBase
from ..models import Reservation
from . import RoomEntity

class ReservationEntity(EntityBase):
    __tablename__ = 'reservation'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    room_name: Mapped[str] = mapped_column(String)
    user_pid: Mapped[int] = mapped_column(Integer)
    start: Mapped[str] = mapped_column(String)
    end: Mapped[str] = mapped_column(String)
    length: Mapped[int] = mapped_column(Integer)

    @classmethod
    def from_model(cls, model: Reservation) -> Self:
        return cls(
            id=model.id,
            room_name=model.room_name,
            user_pid=model.user_pid,
            start=model.start,
            end=model.end,
            length=model.length,
        )

    def to_model(self) -> Reservation:
        return Reservation(
            id=self.id,
            room_name=self.room_name,
            user_pid=self.user_pid,
            start=self.start,
            end=self.end,
            length=self.length,
        )