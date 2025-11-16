import numpy as np

def bayes(prior, likelihood, evidence): 
    return (prior * likelihood) / evidence

prior = 0.3
likelihood = 0.8 
evidence = 0.275

posterior = bayes(prior, likelihood, evidence)
print(f"\nThe updated belief: {posterior:.3f}")

samples_bernoulli = np.random.binomial(n=1, p=0.3, size=10)
print("\nBernoullis distribution: ", samples_bernoulli)

samples_binomial = np.random.binomial(n=10, p=0.5, size=5)
print("\nBinomial Distribution: ", samples_binomial)

samples_normal = np.random.normal(loc=0, scale=1, size=10)
print("\nNormal Distribution: ", samples_normal)