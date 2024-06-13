import numpy as np
import imageio.v3 as iio
from load_image import ft_load
import matplotlib.pyplot as plt
import sys

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError('Error: Only one argument allowed')
    except AssertionError as msg:
        print(msg)
        exit()
    path = sys.argv[1]
    img = ft_load(path)
    print('new shape', img[368:800, 300:700, :1].shape)
    print(img[368:800, 300:700, :1])
    imgplot = plt.imshow(img[100:500, 450:850, :1], cmap='gray')
    plt.show()
if __name__=="__main__": 
    main()
