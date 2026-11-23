
import random
import math

def simulated_annealing():
    current = random.randint(0, 10)
    temperature = 100

    while temperature > 0.1:
        next_state = current + random.choice([-1, 1])

        if next_state < 0 or next_state > 10:
            temperature *= 0.9
            continue

        current_value = -(current - 7) ** 2
        next_value = -(next_state - 7) ** 2

        if next_value > current_value:
            current = next_state
        else:
            probability = math.exp((next_value - current_value) / temperature)

            if random.random() < probability:
                current = next_state

        temperature *= 0.9

    print("Best solution:", current)
    print("Best value:", -(current - 7) ** 2)


simulated_annealing()
