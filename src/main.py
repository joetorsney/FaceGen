"""
Dataset:
http://vision.ucsd.edu/content/yale-face-database

TODO:
- Perform PCA
- Gen new data

"""

import numpy as np
import util
from train import train

ESSEX_PATH = "../data/essexfaces/*"
ESSEX_SHAPE = (180, 200)

if __name__ == "__main__":
    images = util.load_images(ESSEX_PATH)
    print(images.shape)
    print(images[0])
    images = train(images, 16)
    util.display_samples(images, 1, ESSEX_SHAPE)