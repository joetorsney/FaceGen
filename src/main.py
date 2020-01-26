"""
Dataset:
http://vision.ucsd.edu/content/yale-face-database

TODO:
- Load data as np matrix
- Perform PCA
- Gen new data

"""

import numpy as np
from util import load_images

if __name__ == "__main__":
    images = load_images("../data/yalefaces/")