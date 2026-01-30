import numpy as np
import jax
import jax.numpy as jnp

## Exercise 1

# A [128 x 128 x 3] + B [3]
#
# A   128 x 128 x 3
# B     1 x   1 x 3
# -----------------
# A+B 128 x 128 x 3

# A [8 x 1 x 6 x 1] + B [7 x 1 x 5]
#
# A   8 x 1 x 6 x 1
# B       7 x 1 x 5
# -----------------
# A+B 8 x 7 x 6 x 5

# A [2 x 1] + B [8 x 4 x 3]
#
# A           2 x 1
# B       8 x 4 x 3
# -----------------
# A+B         X x 3

# A [3 x 1] + B [15 x 3 x 5]
#
# A           3 x 1
# B      15 x 3 x 5
# -----------------
# A+B    15 x 3 x 5

# A [3] + B [4]
#
# A   3
# B   4
# -----
# A+B X


## Demo 1

rng = np.random.default_rng(1234)
d = rng.normal(
  loc=[-1,0,1], 
  scale=[1,2,3],
  size=(1000,3)
)

d_mean = d.mean(axis=0)
d_std = d.std(axis=0)

d_standardized = ((d - d_mean) / d_std)
d_standardized.mean(axis=0)
d_standardized.std(axis=0)