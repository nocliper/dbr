def mat_pow(M, N):
    """Returns matrix M in N-th power using
    Chebyshev polinomials of second kind
    M – Unimodular matrix
    N – power 

    return = M^N
    """
    import numpy as np
    from scipy.special import eval_chebyu

    p = (M[0,0] + M[1,1])/2

    U_m1 = eval_chebyu(N-1, p)
    U_m2 = eval_chebyu(N-2, p)

    a = M[0,0]*U_m1 - U_m2
    b = M[0,1]*U_m1
    c = M[1,0]*U_m1
    d = M[1,1]*U_m1 - U_m2

    X = np.matrix([[a, b],
                   [c, d]])

    return X
