
from collections import deque

def valid(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3
            and (m == 0 or m >= c)
            and (m == 3 or 3 - m >= 3 - c))

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        m, c, boat = state

        for dm, dc in moves:
            if boat == 1:
                nxt = (m - dm, c - dc, 0)
            else:
                nxt = (m + dm, c + dc, 1)

            if valid(nxt[0], nxt[1]) and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))

    return None

result = solve()

for state in result:
    print(state)
