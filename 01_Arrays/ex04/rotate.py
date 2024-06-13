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
    height, width, c = img[368:800, 300:700, :1].shape
    rotated_img = np.zeros((width, height, c), dtype=img.dtype)
    ##print('new shape', img[368:800, 300:700, :1].shape, ' or (', height, ',', width, ')')
    ##print(img[368:800, 300:700, :1])
    for i in range(height):
        for j in range(width):
            rotated_img[width -1 - j, i] = img[i][j]
    imgplot = plt.imshow(rotated_img, cmap='gray')
    plt.show()
if __name__=="__main__": 
    main()