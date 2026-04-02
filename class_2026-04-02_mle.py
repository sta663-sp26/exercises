import numpy as np
from scipy.stats import gamma
from scipy import optimize

g = gamma(a=2.0, scale=2.0)
x = g.rvs(size=100, random_state=1234)

def mle_gamma(θ): 
  if θ[0] <= 0 or θ[1] <= 0:
    return 1e16
  else:
    return -np.sum(gamma.logpdf(x, a=θ[0], scale=θ[1]))

mle_gamma([1,1])

optimize.minimize(
  mle_gamma, x0=[1,1], method="bfgs"
)

optimize.minimize(
  mle_gamma, x0=[1,1], method="l-bfgs-b",
  bounds=[(1e-8,1e8),(1e-8,1e8)]
)

gamma.fit(x, floc=0)
