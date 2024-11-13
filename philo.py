import threading
import time
import random

def philosopher(index, left_fork, right_fork, iterations):
    for _ in range(iterations):
        print(f"Philosopher {index} is thinking.")
        time.sleep(random.random())
        print(f"Philosopher {index} is hungry.")
        eat(index, left_fork, right_fork)

def eat(index, left_fork, right_fork):
    with left_fork:
        with right_fork:
            print(f"Philosopher {index} is eating.")
            time.sleep(random.random())
            print(f"Philosopher {index} finished eating.")

def dining_philosophers():
    forks = [threading.Lock() for _ in range(5)]
    iterations = int(input("Enter number of iterations for each philosopher: "))
    philosophers = [
        threading.Thread(target=philosopher, args=(i, forks[i % 5], forks[(i + 1) % 5], iterations))
        for i in range(5)
    ]

    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()

# Run the dining philosophers simulation
dining_philosophers()
