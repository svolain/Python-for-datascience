import numpy as np

"""
slice_me take 2D array as parameters y, prints its shape, and returns a
truncated version of the array based on the provided start and end arguments.
"""

def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list) or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError('Error: arguments have wrong type')
        if not all(len(l) == len(family[0]) for l in family):
            raise AssertionError('Error: The elements of 2D array are not same lenght')
        arr = np.array(family)
        print('My shape is : ', arr.shape)
        return arr[start:end].tolist()
    except AssertionError as msg:
        print(msg)
        exit()
    return []