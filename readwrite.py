import threading
import time
import random


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
            print("\nRunning Readers-Writers Problem...")
            readers_writers()

if __name__ == "__main__":
    main()
