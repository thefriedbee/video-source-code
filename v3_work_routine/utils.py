import numpy as np
import pandas as pd
import time


def list_average(lst):
    '''
    Return the average of a numbered list
    lst: a list of numbers
    '''
    return sum(lst)/len(lst)


def list_cumsum2(lst):
    '''
    Return the prodes of all items
    lst: a list of numbers
    '''
    return np.cumsum(lst).tolist()


if __name__ == "__main__":
    # write module tests and exploration here
    lst = list(range(10))
    avg = list_average(lst)
    print('average is:', avg)

    import sys
    print(sys.executable)


