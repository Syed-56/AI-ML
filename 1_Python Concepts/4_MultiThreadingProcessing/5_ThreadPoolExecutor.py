from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

numbers = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    start = time.time()

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_number, numbers)
        for result in results:
            print(result)

    print(f"Total time: {time.time() - start:.2f}s")