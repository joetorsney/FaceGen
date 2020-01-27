import numpy as np
import scipy
from math import sqrt

def train_random_projection(data, k):
    """Performs a random projection of the data into k dimensions.
    Let n be the number of samples
        d be the original number of dimensions
        k be the new number of dimensions
        R be a random matrix
    """
    n, d = data.shape
    print(data.shape)
      
    R = (np.random.choice(3, d*k, p=[1/6, 2/3, 1/6])) - 1
    R = R * sqrt(3)
    R = R.reshape((d, k))

    projected = np.dot((data - np.mean(data)), R)
    return projected

def train_pca(data, n):
    """Calculates the n best PC axes then projects the training data onto them."""
    print("\tCalculating Covariance")
    cov = np.cov(data, rowvar=0)
    N = cov.shape[0]
    print("\tCalculating Eigenvectors")
    e_vals, e_vects = scipy.linalg.eigh(cov, eigvals=(N-n, N-1))
    print("\tFlipping Eigenvector Matrix")
    e_vects = np.fliplr(e_vects)
    print("\tProjecting Data")
    return PCA_project(data, e_vects), e_vects

def PCA_project(data, eigenvects):
    """Projects the given data into the given eigenbasis."""
    return np.dot((data - np.mean(data)), eigenvects)