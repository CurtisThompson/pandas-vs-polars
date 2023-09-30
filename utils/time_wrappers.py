import functools
from datetime import datetime

def repeat(num_times=100, logger=None):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal num_times, logger
            
            # Repeat function n times and store runtimes
            runtimes = []
            for _ in range(num_times):
                stime = datetime.now()
                result = func(*args, **kwargs)
                etime = datetime.now()
                time_taken = (etime - stime).microseconds
                runtimes.append(time_taken)

            # Log results or output if no logger
            time_min = min(runtimes)
            time_max = max(runtimes)
            time_avg = round(sum(runtimes)/num_times, 4)
            time_str = f'{func.__name__}, avg: {time_avg}, min: {time_min}, max: {time_max}'
            if logger == None:
                print(time_str)
            else:
                logger += time_str
            return result
        return wrapper
    return decorator_repeat