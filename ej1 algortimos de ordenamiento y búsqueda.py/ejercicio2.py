import random
import time

def generate_random_list(size):
    return [random.randint(1, 100) for _ in range(size)]

# Generate random lists of different sizes
sizes = [100000, 1000000, 10000000]
lists = [generate_random_list(size) for size in sizes]

# Perform search algorithm and measure execution time
for i, lst in enumerate(lists):
    start_time = time.time()

    # Perform your search algorithm here

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time for list size {sizes[i]}: {execution_time} seconds")

    