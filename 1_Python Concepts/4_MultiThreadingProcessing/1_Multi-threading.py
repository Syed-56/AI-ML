import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)  # simulating an I/O-bound wait
        print(f"Number: {i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)  # simulating an I/O-bound wait
        print(f"Letter: {letter}")

if __name__ == "__main__":
    start = time.time()

    # Create threads
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    # Start threads
    t1.start()
    t2.start()

    # Wait for both to finish before moving on
    t1.join()
    t2.join()

    finished_time = time.time() - start
    print(f"Total time taken: {finished_time:.2f} seconds")