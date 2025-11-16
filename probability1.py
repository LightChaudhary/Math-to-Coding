# Probability and Statistics

import numpy as np 
from statistics import mode

x = np.array([10, 20, 20, 22, 30, 31, 31, 35, 55, 55, 55, 70, 85, 100])
print(np.mean(x).round(3))
print(np.median(x))
print(mode(x))
print(np.std(x).round(3))

science  = np.array([1,1,1,1,0,0,0,0,1,1])
math     = np.array([1,0,1,1,0,1,0,1,1,0])

P_science = np.mean(science == 1)
P_math = np.mean(math == 1)

P_both = np.mean((science == 1) & (math == 1))

P_science_givenmath = P_both / P_math

print()
print("Probability of science: ", P_science)
print("Probability of math: ", P_math)
print("Probability of both: ", P_both)
print("Probability of science given math: ", P_science_givenmath)