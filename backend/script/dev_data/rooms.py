"""Sample rooms"""

from ...models import Room

room1 = Room(id=1, name="A1", max_capacity=3)
room2 = Room(id=2, name="A2", max_capacity=5)

models = [
    room1, 
    room2
]