"""Sample rooms"""

from ...models import Room

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

models = [
    room1, 
    room2
]