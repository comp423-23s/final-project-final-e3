"""Sample reservations"""

from ...models import Reservation

identifier1 = "Room-R1-123456789-1300-0310"

identifier2 = "Monitor-M1-987654321-1400-0310"

reservation1 = Reservation(identifier_id=identifier1, pid=100000000, subject_name="Room-R1", start="13:00-03/10", end="14:00-03/10")
reservation2 = Reservation(identifier_id=identifier2, pid=100000000, subject_name="Monitor-M1", start="14:00-04/30", end="15:00-04/30")

models = [
    reservation1, 
    reservation2
]