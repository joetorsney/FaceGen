## Archived
It's a cool idea, I just don't have time right now!

# This Person *Definitely* Does Not Exist: Creating New Faces From Approximations

## Original Idea
- Approximate some pictures of faces using PCA
- Generate new faces by reintroducing new dimensions, randomly perturbing them from the Principal Components.

## Problems
Performing PCA by calculating the eigenvectors of the covariance matrix requires a huge amount of memory for high-dimensionality data. To proceed, I have chosen to implement a Random projection (Li et al., n.d) (Bingham and Mannila, n.d.). In the future, I may implement a memory efficient PCA algorithm, such as MPOWIT (Rachakonda et al., 2016).

## References

1. Li, P., Hastie, T. and Church, K. (n.d.). Very Sparse Random Projections. [online] Available at: http://web.stanford.edu/~hastie/Papers/Ping/KDD06_rp.pdf [Accessed 27 Jan. 2020].

2. Bingham, E. and Mannila, H. (n.d.). Random projection in dimensionality reduction: Applications to image and text data. [online] Available at: http://users.ics.aalto.fi/ella/publications/randproj_kdd.pdf.

3. Rachakonda, S., Silva, R.F., Liu, J. and Calhoun, V.D. (2016). Memory Efficient PCA Methods for Large Group ICA. Frontiers in Neuroscience, [online] 10. Available at: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4735350/ [Accessed 27 Jan. 2020].
