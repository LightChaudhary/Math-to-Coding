import numpy as np 
import random 

def deterministic_function(x): 
    return (5 * x - 2)

def probabilistic_function(x):
    return (5 * x - 2 + random.uniform(-1 , 1))

x = 5

print('Deterministic output: ', deterministic_function(x))
print('Probabilistic output: ')
for i in range(5): 
    print(probabilistic_function(x))

