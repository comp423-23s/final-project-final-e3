"""Sample reservations"""

from ...models import Reservation

identifier1 = "A1&123456789&13:00-03/10/2023"
identifier2 = "A2&987654321&14:00-03/10/2023"

reservation1 = Reservation(identifier_id=identifier1, pid=123456789, subject_name="A1", start="13:00-03/10/2023", end="14:00-03/10/2023")
reservation2 = Reservation(identifier_id=identifier2, pid=987654321, subject_name="A2", start="14:00-03/10/2023", end="15:00-03/10/2023")

models = [
    reservation1, 
    reservation2
]