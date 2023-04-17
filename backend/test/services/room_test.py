"""Testing room functions"""

import pytest

from sqlalchemy.orm import Session
from ...models import User, Room
from ...entities import RoomEntity
from ...services import RoomService



# Mock room models
room1 = Room(name="A1", max_capacity=3)
room2 = Room(name="A2", max_capacity=5)

# Mock users


@pytest.fixture(autouse=True)
def setup(test_session: Session):
    room1_entity = RoomEntity.from_model(room1)
    test_session.add(room1_entity)

@pytest.fixture()
def room(test_session: Session):
    return RoomService(test_session)

def test_list_room(room: RoomService):
    room_service = room
    rooms = room_service.list()
    assert room1 in rooms

def test_add_room(room: RoomService):
    room_service = room
    room_service.add(2, "A2", 5)
    rooms = room_service.list()
    assert len(rooms) == 2

def test_delete_room(room: RoomService):
    room_service.delete("A1")
    rooms = room_service.list()
    assert len(rooms) == 1