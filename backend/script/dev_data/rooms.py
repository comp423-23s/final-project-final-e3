"""Sample rooms"""

from ...models import Room

availability1 = {
    "Monday": ["08:00", "15:00", "1"],
    "Friday": ["08:00", "17:00", "1"]
}

availability2 = {
    "Monday": ["08:00", "17:00", "1"],
    "Tuesday": ["08:00", "17:00", "1"]
}

room1 = Room(name="A1", max_capacity=3, availability=availability1)
room2 = Room(name="A2", max_capacity=5, availability=availability2)

models = [
    room1, 
    room2
]