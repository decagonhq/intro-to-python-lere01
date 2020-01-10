import time
import functools

def check_time(func):
    """This function returns the total time it takes for a function to run"""
    
    @functools.wraps(func)
    def inner_function(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        
        return '{} took {} seconds to run'.format(func.__name__, duration)
    
    return inner_function