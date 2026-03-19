import numpy as np
import pymc as pm
import arviz as az
import seaborn as sns
import matplotlib.pyplot as plt

## GMM Data

np.random.seed(1234)
x1 = np.random.normal(-2.5, 1, size=1000)
x2 = np.random.normal( 2.5, 1, size=1000)
i = np.random.binomial(1, 0.3, size=1000)
y = np.where(i, x1, x2)

sns.displot({'x': y}, x="x", kind="kde", aspect=1.5)

## GMM Model

with pm.Model() as gmm:
    μ = pm.Normal("μ", mu=0, sigma=5, shape=2)
    σ = pm.HalfNormal("σ", sigma=3, shape=2)
    
    p = pm.Beta("p", 1, 1)
    i = pm.Bernoulli("i", p, shape=len(y))
    
    obs = pm.Normal("y", mu=μ[i], sigma=σ[i], observed=y)

    trace = pm.sample(random_seed=1234, draws=1000, chains=4)

### Summary

az.summary(trace, var_names=["~i"])

### Trace plot

ax = az.plot_trace(trace, var_names=["~i"])
plt.gcf().set_layout_engine("constrained")
plt.show()

### PP

with gmm:
    pp = pm.sample_posterior_predictive(trace, random_seed=1234)
az.plot_ppc(pp)


## GMM Model (revised)

init_mu = np.sort(np.random.normal(size=2))
with pm.Model() as gmm2:
    μ = pm.Normal(
        "μ", mu=0, sigma=10, shape=2,
        transform = pm.distributions.transforms.ordered,
        initval = init_mu
    )
    σ = pm.HalfNormal("σ", sigma=10, shape=2)
    weights = pm.Dirichlet("w", np.ones(2))

    obs = pm.NormalMixture("y", w=weights, mu=μ, sigma=σ, observed=y)
    trace = pm.sample(random_seed=1234, draws=1000)
