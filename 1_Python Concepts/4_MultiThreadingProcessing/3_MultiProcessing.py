import multiprocessing
import time

def square_numbers():
    result = []
    for i in range(10**7):
        result.append(i * i)   # actual CPU work, no sleep

def cube_numbers():
    result = []
    for i in range(10**7):
        result.append(i * i * i)

if __name__ == "__main__":
    start = time.time()
    square_numbers()
    cube_numbers()
    print(f"Sequential: {time.time() - start:.2f}s")
    
    start = time.time()
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Multi Processing: {time.time() - start:.2f}s")