# Matrix Decomposition (SVD, PCA basics)

import numpy as np 

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

U, S, VT = np.linalg.svd(A)

print("\nLeft Singular Vector (U): \n", U)
print("\nSingular Values (S): \n", S)
print("\nRight Singular Vector (V^T): \n", VT)

X = np.array([
    [2.5, 2.4], 
    [0.5, 0.7],
    [2.2, 2.9]
])

X_centered = X - X.mean(axis=0)

u, s ,vT = np.linalg.svd(X_centered)

components = vT[:2]

print("\nPrincipal components:\n", components)

X_reduced = X_centered @ components.T
print("\nReduced Data:\n", X_reduced)