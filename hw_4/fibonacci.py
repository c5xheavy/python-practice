import time
import threading
import multiprocessing
import os

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    n = 35
    num_runs = 10

    sync_times = []
    start_time = time.time()
    for _ in range(num_runs):
        fibonacci(n)
    end_time = time.time()
    sync_total_time = end_time - start_time

    thread_times = []
    threads = []
    start_time = time.time()
    for _ in range(num_runs):
        thread = threading.Thread(target=fibonacci, args=(n, ))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    thread_total_time = end_time - start_time

    process_times = []
    processes = []
    start_time = time.time()
    for _ in range(num_runs):
        process = multiprocessing.Process(target=fibonacci, args=(n, ))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    process_total_time = end_time - start_time

    with open('fibonacci.txt', 'w') as f:
        f.write(f'sync total time: {sync_total_time:.4f}s\n')
        f.write(f'thread total time: {thread_total_time:.4f}s\n')
        f.write(f'process total time: {process_total_time:.4f}s\n')
