import random

chain = {
    "Sunny": ["Sunny", "Rainy"],
    "Rainy": ["Sunny", "Rainy"]
}

state = "Sunny"

for i in range(5):
    print(state)
    state = random.choice(chain[state])
