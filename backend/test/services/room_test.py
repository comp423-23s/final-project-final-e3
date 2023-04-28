"""Testing room service functions"""

import pytest

from sqlalchemy.orm import Session
from ...models import User, Room
from ...entities import RoomEntity
from ...services import RoomService


# Mock room models
availability1 = {
    "Sunday": ["12:00", "13:00", "1"],
    "Monday": ["13:00", "14:00", "1"],
    "Tuesday": ["14:00", "15:00", "1"],
    "Wednesday": ["15:00", "16:00", "1"],
    "Thursday": ["16:00", "17:00", "1"],
    "Friday": ["17:00", "18:00", "0.5"],
    "Saturday": ["18:00", "19:00", "1"]
}

availability2 = {
    "Sunday": ["12:00", "13:00", "1"],
    "Monday": ["13:00", "14:00", "1"],
    "Tuesday": ["14:00", "15:00", "1"],
    "Wednesday": ["15:00", "16:00", "1"],
    "Thursday": ["16:00", "17:00", "1"],
    "Friday": ["17:00", "18:00", "0.5"],
    "Saturday": ["18:00", "19:00", "1"]
}

deviation1 = {}

deviation2 = {}

room1 = Room(name="A1", max_capacity=3, availability=availability1, deviations=deviation1)
room2 = Room(name="A2", max_capacity=5, availability=availability2, deviations=deviation2)


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
    room_service.add(100000002, room2)
    rooms = room_service.list()
    assert len(rooms) == 2

def test_delete_room(room: RoomService):
    room_service.delete("A1")
    rooms = room_service.list()
    assert len(rooms) == 1