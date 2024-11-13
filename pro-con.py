import threading
import time
import random

# Shared buffer and maximum buffer size
buffer = []
buffer_size = 5

# Semaphores
empty = threading.Semaphore(buffer_size)  # Tracks empty slots
full = threading.Semaphore(0)             # Tracks filled slots
mutex = threading.Lock()                  # Mutex for buffer access

# Producer Function
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

producer_consumer();
