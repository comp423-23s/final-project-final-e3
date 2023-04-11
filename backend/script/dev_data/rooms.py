"""Sample rooms"""

from ...models import Room

availability1 = {
    "Monday": ["12:34:56-01/01/2001", "20:34:56-01/01/2001", "1"],
    "Friday": ["21:43:59-02/02/2002", "22:00:59-02/02/2002", "0.5"]
}

availability2 = {
    "Monday": ["12:34:56-01/01/2001", "20:34:56-01/01/2001", "1"],
    "Friday": ["21:43:59-02/02/2002", "20:34:56-01/01/2001", "1"]
}

room1 = Room(name="A1", max_capacity=3, availability=availability1)
room2 = Room(name="A2", max_capacity=5, availability=availability2)

models = [
    room1, 
    room2
]