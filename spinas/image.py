import numpy as np

def rebin_image(image, size):
    """Rebin image using a square cluster of size x size pixels"""
    new = np.zeros( np.floor(np.asarray(image.shape)/size).astype(np.int))
    for i in range(size):
        for j in range(size):
            new += image[i::size, j::size][0:new.shape[0], 0:new.shape[1]]
    return new