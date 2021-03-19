
def mat_trans(l_1, n_1, l_2, n_2, l_s, n_s, wl, N, n_0):
    """Returns transfer matrices of DBR with
    l_1 – First layer thickness
    l_2 – Second layer thickness
    l_s – Substrate thickness
    wl  – Wavelenght
    N   – Number of superlattice layers
    """

    import numpy as np
    from mat_pow import mat_pow

    def generate_matrix(n_1, n_2, l_2, wl):
        """Returns transfer matrix of a n_1/n_2 border
        reflected wave and passed n_2 region with l_2 thickness

        ....|  (n_1)  |  (n_2)  |
        ....|         |         |
        ....|       ~>|~~~~~~~~>|
        ....|         |         |
        ....|         |<--l_2-->|

        """

        M1 = np.matrix([[n_2(wl) + n_1(wl), n_2(wl) - n_1(wl)],
                        [n_2(wl) - n_1(wl), n_2(wl) + n_1(wl)]])
        M1 = M1/(2*n_2(wl))

        k  = 2*np.pi*n_2(wl)/wl
        T  = l_2

        M2 = np.matrix([[np.exp(1j*k*T),                0],
                        [0             , np.exp(-1j*k*T)]])
        return M1@M2

    ## Air/First layer:
    M01 = generate_matrix(n_0, n_1, l_1, wl)
    ## First/Second layer
    M12 = generate_matrix(n_1, n_2, l_2, wl)
    M21 = generate_matrix(n_2, n_1, l_1, wl)
    ML  = M12@M21
    ML  = mat_pow(ML, N)
    ## Second/Substrate layer
    M2S = generate_matrix(n_2, n_s, l_s, wl)

    #M = M01@ML@M2S # air and substrate
    M = ML@M2S  #substrate
    #M = M01@ML #air
    #M = ML # only layers

    return M
