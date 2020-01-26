"""
Dataset:
http://vision.ucsd.edu/content/yale-face-database

TODO:
- Load data as np matrix
- Perform PCA
- Gen new data

"""

import numpy as np
import util

if __name__ == "__main__":
    images = util.load_images("../data/yalefaces/")
    util.display_samples(images, 1, images.shape[1:])