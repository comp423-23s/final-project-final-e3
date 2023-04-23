"""Sample reservations"""

from ...models import Reservation

import hashlib

identifier1 = "A1&123456789&13:00-03/10"
identifier1_hashed = hashlib.sha256(identifier1.encode()).hexdigest()

identifier2 = "A2&987654321&14:00-03/10"
identifier2_hashed = hashlib.sha256(identifier2.encode()).hexdigest()

reservation1 = Reservation(identifier_id=identifier1_hashed, pid=123456789, subject_name="A1", start="13:00-03/10", end="14:00-03/10")
reservation2 = Reservation(identifier_id=identifier2_hashed, pid=987654321, subject_name="A2", start="14:00-03/10", end="15:00-03/10")

models = [
    reservation1, 
    reservation2
]