"""
Load functions supporting the generator system.
"""

import glob
import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def load_images(path):
    images = []
    for im_path in glob.glob(path+"*"):
        images.append(imageio.imread(im_path))

    return np.array(images)

def display_samples(data, start, shape=(243, 320)):
    """Displays 16 samples from start in a subplot."""
    for i in range(0, 16):
        plt.subplot(4, 4, i+1)
        display_sample(data, start + i, shape)
    plt.show()

def display_sample(data, n, shape=(243, 320)):
    """Displays sample n"""
    letter_image = np.reshape(data[n, :], shape, order='F').transpose()
    plt.imshow(letter_image, cmap=cm.Greys_r)