import numpy as np 
from scipy import stats

data = np.array([1,1,0,1,0,1,1,1,1,0])
heads = data.sum()
tails = len(data) - heads

def likelihood(p): 
    return (p ** heads ) * ((1-p) ** tails)

for p in [0.1, 0.5, 0.75, 0.9]: 
    print(p, likelihood(p))

print()

X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 6, 8, 10])

cov = np.cov(X, Y)[0][1]
corr = np.corrcoef(X, Y)[0][1]

print("Covariance: ", cov)
print("Correlation: ", corr.round(2))
print()

model_A = np.array([0.80, 0.82, 0.79, 0.81, 0.83])
model_B = np.array([0.84, 0.85, 0.83, 0.86, 0.87])

t, p = stats.ttest_ind(model_A, model_B)

print("t-statistics: ", t)
print("p-value: ", p)

print()
true = np.array([1,0,0])
pred1 = np.array([0.7, 0.2, 0.1])  
pred2 = np.array([0.01, 0.7, 0.29])

ce1 = -np.log(pred1[0])
ce2 = -np.log(pred2[0])

print("Cross entropy(good): ", ce1)
print("Cross entropy(bad): ", ce2)