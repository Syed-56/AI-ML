import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(1_000_000)

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    return result

if __name__ == "__main__":
    numbers = [6000, 7000, 8000]

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    for num, result in zip(numbers, results):
        print(f"Factorial of {num} has {len(str(result))} digits")

    print(f"Time taken: {end_time - start_time:.4f} seconds")