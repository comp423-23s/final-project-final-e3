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

deviation1 = {"04/28": ["13:13", "19:19", "0.5"], 
              "03/14": ["03:03", "04:03", "1"]}

deviation2 = {}

room1 = Room(name="Room-R1", max_capacity=3, availability=availability1, deviations=deviation1)
room2 = Room(name="Monitor-M1", max_capacity=1, availability=availability2, deviations=deviation2)

models = [
    room1, 
    room2
]