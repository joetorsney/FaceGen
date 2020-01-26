"""
Load functions supporting the generator system.
"""

import glob
import imageio
import numpy as np

def load_images(path):
    images = []
    for im_path in glob.glob(path+"*"):
        images.append(imageio.imread(im_path))

    return np.array(images)