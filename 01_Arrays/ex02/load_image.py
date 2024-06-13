import numpy as np
import imageio.v3 as iio
import array

"""
ft_load loads an image, prints its format, and its pixels
content in RGB format.
"""

def ft_load(path: str) -> array:
    try:
        if not isinstance(path, str):
            raise AssertionError('Error:argument is not a string')
        img = iio.imread(path)
        if img is None:
            raise AssertionError('Error: image can\'t be loaded')
        print('The shape of image is: ',img.shape)
        print(img)
        return img    
    except AssertionError as msg:
        print(msg)
        exit()
        return []
