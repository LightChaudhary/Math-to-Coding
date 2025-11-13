# Vector And Matrices
# Representation

import numpy as np

x = np.array([12, 55, 88])
print("Vector\n: ", x)
print("Shape: ", x.shape)
print("Dimension: ", x.ndim)

X = np.array([
    [12, 45, 78, 90],
    [16, 46, 57, 78],
    [20, 80, 90, 91]
])

print("\nDataset: \n", X)
print("Samples: ", X.shape[0])
print("Features: ", X.shape[1])

# Matrix Operations 

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print("\nAddition: \n", a + b)
print("\nSubtraction: \n", a - b)
print("\nElement-wise Multiplication: \n", a * b) 
print("\nMatrix Multiplication: \n", np.dot(a,b) )
print("\nMatrix Transpose: \n", a.T)

a_inv = np.linalg.inv(a) 
print("\nInverse: \n", a_inv)

print("\nIdentity Matrix: \n", np.dot(a, a_inv).round(2))

I = np.eye(3)
print("\nIdentity Matrix: \n", I)

D = np.diag([2, 4, 6])
print("Diagonal Matrix: ", D)