"""Sample equipment"""

from ...models import Equipment

availability1 = {
    "Monday": ["12:34:56-01/01/2001", "20:34:56-01/01/2001", "1"],
    "Friday": ["21:43:59-02/02/2002", "22:00:59-02/02/2002", "0.5"]
}

availability2 = {
    "Monday": ["12:34:56-01/01/2001", "20:34:56-01/01/2001", "1"],
    "Friday": ["21:43:59-02/02/2002", "20:34:56-01/01/2001", "1"]
}

equipment1 = Equipment(name="Monitor-M1", availability=availability1)
equipment2 = Equipment(name="Monitor-M2", availability=availability2)

models = [
    equipment1, 
    equipment2
]