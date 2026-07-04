from multiprocessing import Process, Queue

def worker(q):
    q.put("result from child process")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    p.join()
    print(q.get())  # "result from child process"