import numpy as np
from scipy import optimize
import timeit

def f(x):
    return np.exp(x[0]-1) + np.exp(-x[1]+1) + (x[0]-x[1])**2

def grad(x):
    return [
        np.exp(x[0]-1) + 2*(x[0] - x[1]),
        -np.exp(-x[1]+1) - 2*(x[0]-x[1])
    ]

x0 = [0,0]

optimize.minimize(fun=f, x0=x0, jac = grad, method="bfgs")
optimize.minimize(fun=f, x0=x0, jac = grad, method="CG")
optimize.minimize(fun=f, x0=x0, jac = grad, method="newton-cg")
optimize.minimize(fun=f, x0=x0, method="nelder-mead")

timeit.Timer(
    lambda: optimize.minimize(fun=f, x0=x0, jac = grad, method="bfgs")
).repeat(1,100)

timeit.Timer(
    lambda: optimize.minimize(fun=f, x0=x0, jac = grad, method="CG")
).repeat(1,100)

timeit.Timer(
    lambda: optimize.minimize(fun=f, x0=x0, jac = grad, method="newton-cg")
).repeat(1,100)

timeit.Timer(
    lambda: optimize.minimize(fun=f, x0=x0, method="nelder-mead")
).repeat(1,100)
