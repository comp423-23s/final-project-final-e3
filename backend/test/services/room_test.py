import pytest

from sqlalchemy.orm import Session
from ...models import Room
from ...entities import room_entity
from ...services import room_service

# Mock models
room1 = Room(id=1, name="A1", max_capacity=3)

@pytest.fixture(autouse=True)
def setup(test_session: Session):
    room1_entity = RoomEntity.from_model(room1)
    test_session.add(room1_entity)

@pytest.fixture()
def room(test_session: Session):
    return RoomService(test_session)

def test_list_room(room_service: RoomService):
    rooms = room_serivice.list()
    assert rooms is list[Room]
    assert room1 in rooms

def test_add_room(room_service: RoomService):
    room_service.add(2, "A2", 5)
    rooms = room_serivice.list()
    assert len(rooms) == 2