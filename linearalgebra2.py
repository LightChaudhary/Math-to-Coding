# Dot product and Matrix Multiplication

import numpy as np 

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

print("Dot product:", a @ b)

X = np.array([
    [1, 2, 3],
    [3, 4, 5]
])
W = np.array([
    [1, 2], 
    [3, 3], 
    [4, 5]
])
Y_pred = X @ W

print("\nPredicted outputs: \n", Y_pred)

# Eigenvalues and Eigenvectors

A = np.array([
    [9, 0],
    [0, 4]
])
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues: \n", eigenvalues.round(2))
print("\nEigenvectors: \n", eigenvectors.round(2))

# Norm and Projectons

l1_norm = np.linalg.norm(X, 1)
l2_norm = np.linalg.norm(X,2)
l_inf_norm = np.linalg.norm(X, np.inf)

print("\nL1 norm: ", l1_norm)
print("L2 norm: ", l2_norm)
print("L infinite norm: ", l_inf_norm)

a = np.array([1, 2])
b = np.array([0, 1])

proj_b_a = (np.dot(a,b) / np.dot(b,b)) * b

print("\nProjection of a onto b: ", proj_b_a)