"""Sample equipments"""

from ...models import Equipment

availability1 = {
    "Monday": ["08:00", "15:00", "1"],
    "Friday": ["08:00", "17:00", "1"]
}

availability2 = {
    "Monday": ["08:00", "17:00", "1"],
    "Tuesday": ["08:00", "17:00", "1"]
}

equipment1 = Equipment(name="E1", availability=availability1)
equipment2 = Equipment(name="E2", availability=availability2)

models = [
    equipment1,
    equipment2
]