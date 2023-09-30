import functools
from time import perf_counter_ns
from statistics import mean, stdev, median

def repeat(num_times=100, logger=None):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal num_times, logger

            # Repeat function n times and store runtimes as microseconds
            runtimes = []
            for _ in range(num_times):
                stime = perf_counter_ns()
                result = func(*args, **kwargs)
                etime = perf_counter_ns()
                time_taken = (etime - stime) // 1000
                runtimes.append(time_taken)

            # Log results or output if no logger
            time_min = min(runtimes)
            time_max = max(runtimes)
            time_avg = round(mean(runtimes))
            time_med = round(median(runtimes))
            time_std = round(stdev(runtimes))
            time_str = f'{func.__name__}, mean: {time_avg}, med: {time_med}, min: {time_min}, max: {time_max}, std: {time_std}'
            if logger == None:
                print(time_str)
            else:
                logger += time_str
            return result
        return wrapper
    return decorator_repeat