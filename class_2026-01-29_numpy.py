import numpy as np

np.array([1,2,3])

## Exercise 1

x = np.arange(16).reshape((4,4)); x

x[1:3, 1:3]
x[(1,2),(1,2)]
x[[1,2],[1,2]]

np.shares_memory(x, x[1:3, 1:3])
np.shares_memory(x, )
np.shares_memory(x, x[[1,2],[1,2]])


## Exercise 2

pts = np.linspace(-1, 2, 3001)
x, y = np.meshgrid(pts, pts)

f = (1-x)**2+100*(y-x**2)**2
np.min(f)

x[f == np.min(f)]
y[f == np.min(f)]

min_i = np.argmin(f, axis=None)
x.reshape(-1)[min_i]
y.ravel()[min_i]
