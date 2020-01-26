import numpy as np

def train(data, n):
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