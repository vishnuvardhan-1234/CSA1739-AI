import numpy as np

Q = np.zeros((3, 2))
reward = [[0, 1], [0, 1], [0, 0]]

for i in range(100):
    state = np.random.randint(3)
    action = np.argmax(Q[state])
    Q[state][action] += 0.1 * (
        reward[state][action] - Q[state][action])

print("Q Table:")
print(Q)
