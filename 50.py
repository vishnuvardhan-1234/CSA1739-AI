import numpy as np

population = np.random.rand(10, 4)

for i in range(50):
    fitness = 1 / (1 + np.sum(population**2, axis=1))

    best = population[np.argmax(fitness)]

    new = []
    for j in range(10):
        child = best + np.random.randn(4) * 0.1
        new.append(child)

    population = np.array(new)

print("Best Weights:", best)
print("Best Fitness:", max(fitness))
