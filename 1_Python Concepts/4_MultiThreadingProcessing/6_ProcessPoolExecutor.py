from concurrent.futures import ProcessPoolExecutor
import time

def square(number):
    time.sleep(2)
    return number * number

numbers = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    start = time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)
        for result in results:
            print(result)

    print(f"Total time: {time.time() - start:.2f}s")