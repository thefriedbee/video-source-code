# decorator
import time, logging


# EXAMPLE 1. time a function
def timeit_1(input_function):
    t1 = time.time() # start
    input_function()
    t2 = time.time() # end
    print( 'the function {} takes {:.2f} seconds'.format(input_function.__name__, t2 - t1) )

def dumb_sleeper(sec = 0.5):
    time.sleep(sec)
    print('dumb executed!')

# timeit_1(dumb_sleeper)


# EXAMPLE 2. time a function using closure structure
def timeit_2(input_function):
    def output_function():
        t1 = time.time() # start
        input_function()
        t2 = time.time() # end (only executed after input function)
        print( 'the function {} takes {:.2f} seconds'.format(input_function.__name__, t2 - t1) )

    return output_function

dumb_sleeper_out = timeit_2(dumb_sleeper)
# dumb_sleeper_out()
# dumb_sleeper_out()
# dumb_sleeper_out()
# dumb_sleeper_out()


# EXAMPLE 3. build a COMPLETE timer
@timeit_2
def dumb_sleeper(sec = 0.5):
    time.sleep(sec)
    print('dumb executed!')

# dumb_sleeper()
# dumb_sleeper(sec = 1) # error


# decorator requirements
# 1. input the same
# 2. output the same
# 3. input function is executed as it should be
# 4. achieve the function required
def timeit_3(input_function):
    # print( 'run {} factory'.format(timeit_3.__name__) )
    def output_function(*args, **kwargs):
        t1 = time.time() # start
        results = input_function(*args, **kwargs)
        t2 = time.time() # end (only executed after input function)
        print( 'the function {} takes {:.2f} seconds'.format(input_function.__name__, t2 - t1) )

        return results # return the same results

    return output_function

@timeit_3
def dumb_sleeper(sec = 0.5):
    time.sleep(sec)
    print('dumb executed!')

# dumb_sleeper()
# dumb_sleeper(sec = 1) # no error this time!
# dumb_sleeper(sec = 1.2)










# EXAMPLE 4 Chaining decorators

from functools import wraps


def trace(func):
    import logging
    logging.basicConfig(filename='history.log', level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_str = '{}({}, {}) -> {}'.format(func.__name__, args, kwargs, result)
        print(log_str)
        logging.info(log_str)

        return result
    return wrapper


def timeit_3(input_function):
    # print( 'run {} factory'.format(timeit_3.__name__) )

    @wraps(input_function)
    def output_function(*args, **kwargs):
        t1 = time.time() # start
        results = input_function(*args, **kwargs)
        t2 = time.time() # end (only executed after input function)
        print( 'the function {} takes {:.2f} seconds'.format(input_function.__name__, t2 - t1) )

        return results # return the same results

    return output_function


# chain trace and log at the same time
@trace
@timeit_3
def dumb_sleeper(sec = 0.5):
    time.sleep(sec)
    print('dumb executed!')

# dumb_sleeper(sec = 1) # logging trace information incorrect


print(dir(dumb_sleeper))
