"""Testing reservation service functions"""

import pytest

from sqlalchemy.orm import Session
from ...models import Reservation
from ...entities import ReservationEntity
from ...services import ReservationService

# Mock reservation models
identifier1 = "A1&123456789&13:00-03/10/2023"
identifier2 = "A2&987654321&14:00-03/10/2023"

reservation1 = Reservation(identifier_id=identifier1, pid=123456789, subject_name="A1", start="13:00-03/10/2023", end="14:00-03/10/2023")
reservation2 = Reservation(identifier_id=identifier2, pid=987654321, subject_name="A2", start="14:00-03/10/2023", end="15:00-03/10/2023")

@pytest.fixture(autouse=True)
def setup(test_session: Session):
    reservation1_entity = ReservationEntity.from_model(reservation1)
    test_session.add(reservation1_entity)

@pytest.fixture()
def reservation_service(test_session: Session):
    return ReservationService(test_session)

def test_list_reservation(reservation_service: ReservationService):
    reservations = reservation_service.list(123456789)
    assert reservation1 in reservations

def test_add_reservation(reservation_service: ReservationService):
    reservation_service.add(reservation2)
    reservations = reservation_service.list_all()
    assert len(reservations) == 2

def test_list_all(reservation_service: ReservationService):
    reservations = reservation_service.list_all()
    assert reservation2 in reservations

def test_delete_reservation(reservation_service: ReservationService):
    reservation_service.delete("A2&987654321&14:00-03/10/2023")
    reservations = reservation_service.list_all()
    assert len(reservations) == 1
