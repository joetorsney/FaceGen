"""
Dataset:
http://vision.ucsd.edu/content/yale-face-database

TODO:
- Perform PCA
- Gen new data

"""

import numpy as np
import util
from train import train_random_projection

ESSEX_PATH = "../data/essexfaces/*"
ESSEX_SHAPE = (180, 200)

if __name__ == "__main__":
    images = util.load_images(ESSEX_PATH)
    images = train_random_projection(images, 16)
    print(images.shape)
    print(images[0])
    util.display_samples(images, 1, ESSEX_SHAPE)