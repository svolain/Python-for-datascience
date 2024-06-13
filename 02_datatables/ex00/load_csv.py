import pandas as pd

"""
load takes a path to dataset as argument, writes the dimensions of the data set
and returns it.
"""

def load(path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(path)
    except FileNotFoundError:
        print('Error: file doesnt exit')
        exit()
    shape = data.shape
    print('Loading dataset of dimensions {}'.format(shape))
    return data