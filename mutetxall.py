import threading
import time
import random

# Producer-Consumer Problem
def producer_consumer():
    buffer = []
    buffer_size = int(input("Enter buffer size for Producer-Consumer: "))
    max_items = int(input("Enter the number of items to produce and consume: "))
    buffer_lock = threading.Lock()
    empty = threading.Semaphore(buffer_size)
    full = threading.Semaphore(0)

    def producer():
        for _ in range(max_items):
            item = random.randint(1, 100)
            empty.acquire()
            buffer_lock.acquire()
            buffer.append(item)
            print(f"Producer produced: {item}")
            buffer_lock.release()
            full.release()
            time.sleep(random.random())

    def consumer():
        for _ in range(max_items):
            full.acquire()
            buffer_lock.acquire()
            if buffer:
                item = buffer.pop(0)
                print(f"Consumer consumed: {item}")
            buffer_lock.release()
            empty.release()
            time.sleep(random.random())

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

# Dining Philosophers Problem
def dining_philosophers():
    class Philosopher(threading.Thread):
        def __init__(self, index, left_fork, right_fork, iterations):
            threading.Thread.__init__(self)
            self.index = index
            self.left_fork = left_fork
            self.right_fork = right_fork
            self.iterations = iterations

        def run(self):
            for _ in range(self.iterations):
                print(f"Philosopher {self.index} is thinking.")
                time.sleep(random.random())
                print(f"Philosopher {self.index} is hungry.")
                self.eat()

        def eat(self):
            with self.left_fork:
                with self.right_fork:
                    print(f"Philosopher {self.index} is eating.")
                    time.sleep(random.random())
                    print(f"Philosopher {self.index} finished eating.")

    forks = [threading.Lock() for _ in range(5)]
    iterations = int(input("Enter number of iterations for each philosopher: "))
    philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5], iterations) for i in range(5)]

    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()

# Readers-Writers Problem
def readers_writers():
    mutex = threading.Lock()
    write_block = threading.Lock()
    readers_count = 0
    read_operations = int(input("Enter number of read operations: "))
    write_operations = int(input("Enter number of write operations: "))

    def reader():
        nonlocal readers_count
        for _ in range(read_operations):
            mutex.acquire()
            readers_count += 1
            if readers_count == 1:
                write_block.acquire()
            mutex.release()

            print(f"Reader {threading.current_thread().name} is reading.")
            time.sleep(1)
            print(f"Reader {threading.current_thread().name} finished reading.")

            mutex.acquire()
            readers_count -= 1
            if readers_count == 0:
                write_block.release()
            mutex.release()

            time.sleep(1)

    def writer():
        for _ in range(write_operations):
            print(f"Writer {threading.current_thread().name} is waiting to write.")
            write_block.acquire()

            print(f"Writer {threading.current_thread().name} is writing.")
            time.sleep(2)
            print(f"Writer {threading.current_thread().name} finished writing.")

            write_block.release()
            time.sleep(1)

    for i in range(3):
        threading.Thread(target=reader, name=f'Reader-{i+1}').start()

    for i in range(2):
        threading.Thread(target=writer, name=f'Writer-{i+1}').start()

# Main Function with Menu (Switch Case)
def main():
    while True:
        print("\n--- Synchronization Problems Menu ---")
        print("1. Producer-Consumer Problem")
        print("2. Dining Philosophers Problem")
        print("3. Readers-Writers Problem")
        print("4. Exit")

        choice = int(input("Choose a problem to run (1-4): "))

        if choice == 1:
            print("\nRunning Producer-Consumer Problem...")
            producer_consumer()
        elif choice == 2:
            print("\nRunning Dining Philosophers Problem...")
            dining_philosophers()
        elif choice == 3:
            print("\nRunning Readers-Writers Problem...")
            readers_writers()
        elif choice == 4:
            print("\nExiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
