import math
import concurrent.futures
import logging
import time
import os
import multiprocessing

def integrate_chunk(f, a, b, chunk_size, chunk_index):
    acc = 0
    step = (b - a) / chunk_size
    start = a + chunk_index * step
    for i in range(chunk_size):
        acc += f(start + i * step) * step
    logging.info(f"Process {os.getpid()} finished chunk {chunk_index}")
    return acc

def integrate(f, a, b, cpu_num, *, n_jobs=1, n_iter=10000000):
    chunk_size = n_iter // n_jobs
    
    if n_jobs == 1:
        return integrate_chunk(f, a, b, n_iter, 0)

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
      futures = [executor.submit(integrate_chunk, f, a, b, chunk_size, i) for i in range(n_jobs)]
      result = sum(future.result() for future in concurrent.futures.as_completed(futures))
    return result

def benchmark(executor_type, f, a, b, n_iter, cpu_num):
    results = []
    for n_jobs in range(1, cpu_num * 2 + 1):
        start_time = time.time()
        if executor_type == "ThreadPoolExecutor":
            with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
                futures = [executor.submit(integrate_chunk, f, a, b, n_iter // n_jobs, i) for i in range(n_jobs)]
                result = sum(future.result() for future in concurrent.futures.as_completed(futures))
        elif executor_type == "ProcessPoolExecutor":
            result = integrate(f, a, b, cpu_num, n_jobs=n_jobs, n_iter=n_iter)
        else:
            raise ValueError("Invalid executor type")
        end_time = time.time()
        results.append((n_jobs, end_time - start_time))
    return results


if __name__ == "__main__":
    logging.basicConfig(filename='integrate_log.txt', level=logging.INFO, 
                        format='%(asctime)s - %(processName)s - %(message)s')

    cpu_num = multiprocessing.cpu_count()
    n_iter = 10000000

    thread_results = benchmark("ThreadPoolExecutor", math.cos, 0, math.pi / 2, n_iter, cpu_num)
    process_results = benchmark("ProcessPoolExecutor", math.cos, 0, math.pi / 2, n_iter, cpu_num)

    with open('integrate_result.txt', 'w') as f:
        f.write("ThreadPoolExecutor results:\n")
        for n_jobs, time_taken in thread_results:
            f.write(f"n_jobs: {n_jobs}, time: {time_taken:.4f}s\n")
        f.write("\nProcessPoolExecutor results:\n")
        for n_jobs, time_taken in process_results:
            f.write(f"n_jobs: {n_jobs}, time: {time_taken:.4f}s\n")
