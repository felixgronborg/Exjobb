import matplotlib.pyplot as plt
import numpy as np
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean


def resize(image_list = [], scale = 1):
    scaled_list = []
    for i in range(len(image_list)):
        im = np.array(image_list[i])

        rows = round(im.shape[0] * scale)
        cols = round(im.shape[1] * scale)
        dims = im.shape[2]

        im_scaled = np.empty((rows, cols, dims))
        for i in range (0,3):
            im_scaled[:,:,i] = rescale(im[:,:,i], scale, anti_aliasing = False)
        scaled_list.append(im_scaled)
        print(len(scaled_list), 'images scaled')

    imgplot = plt.imshow(scaled_list[0])
    plt.show()
    return scaled_list