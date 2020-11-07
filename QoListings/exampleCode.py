import numpy as np

def getA(order, scheme = "central"):
    # Returns the $a$ array for a given order. By default, it returns the values of $a$ for the
    # central difference scheme, but this can be changed by using
    #
    #       scheme = "forward"
    # or
    #       scheme = "backward"
    from numpy.linalg import solve

    if order % 2 == 1:
        raise ValueError("\n\n\tArgument \"order\" must be divisible by 2.\n\n")

    aSize = int(order / 2)
    # Let $M a = P$

    if scheme.lower() == "central":
        M = np.zeros([aSize, aSize])

        for i in range(aSize):

            for j in range(aSize):
                M[i, j] = (j + 1) ** (2 * i + 1)

        P = np.zeros([aSize])
        P[0] = 1 / 2
        a = solve(M, P)
    else:
        M = np.zeros([order, order])

        for i in range(order):

            for j in range(order):
                M[i, j] = (j + 1) ** (i + 1)

        P = np.zeros([order])
        P[0] = 1
        a = solve(M, P)
        print(r"$\int \limits _0 ^{\infty} \text{e}^{-x^2} \text{d} x$")
    return a
