import numpy as np
import imageio.v3 as iio
import array

"""
ft_load loads an image, prints its format, and its pixels
content in RGB format.
"""

def ft_load(path: str) -> array:
    try:
        img = iio.imread(path)
    except FileNotFoundError:
        print('Error: file doesnt exit')
        exit()
    print('The shape of image is: ',img.shape)
    print(img)
    return img