
from collections import deque

def water_jug():
    start = (0, 0)
    goal = 2
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == goal:
            return path

        amount = min(a, 3 - b)
        states = [
            (4, b),                 # Fill 4-litre jug
            (a, 3),                 # Fill 3-litre jug
            (0, b),                 # Empty 4-litre jug
            (a, 0),                 # Empty 3-litre jug
            (a - amount, b + amount), # Pour 4 into 3
        ]

        amount = min(b, 4 - a)
        states.append((a + amount, b - amount))  # Pour 3 into 4

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    return None

result = water_jug()

for state in result:
    print(state)
