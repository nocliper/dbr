
def reflectance(M):
    """Returns reflectance """

    import numpy as np

    R = np.abs(-M[1,0]/M[1,1])**2

    return R
