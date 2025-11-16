# Chain Rule 

import numpy as np 

x = 2.0 
w = 0.5
y = 1.0 

z = w * x 
a = 1 / (1 + np.exp(-z))
loss = (a - y)**2

dloss_da = 2 * (a - y)
da_dz = a * (1 - a)
dz_dw = x

dloss_dw = dloss_da * da_dz * dz_dw
print(f"Loss derivative w.r.t w: {dloss_dw:.3f}")