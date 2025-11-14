# Derivatives & Partial Derivatives
import sympy as sp

x, y = sp.symbols("x y")

f = x**2 + x*y + y**2

df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

print("Differentiation w.r.t x: ", df_dx)
print("\nDifferentiation w.r.t y:", df_dy)

import numpy as np

# loss function L(W) = (w-3)**2

w = np.array([0.0])
n = 0.1
print()

for i in range(10): 
    grad = 2*(w-3)
    w -= n * grad
    print(f"Step{i+1}: w= {w[0]:.3f}")

# Multi-Variable 

w1, w2 = 0 , 0
lr = 0.2
print()

for i in range(10): 
    grad1 = 2 * (w1 - 2)
    grad2 = 2 * (w2 + 2)
    w1 -= lr * grad1
    w2 -= lr * grad2
    print(f"Step{i+1}: w1 = {w1:.3f}, w2 = {w2:.3f}")