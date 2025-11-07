import random

trails = 1000000
even = 0
greater_than4 = 0
either = 0

for _ in range(trails): 
    roll = random.randint(1,6)
    is_even = (roll % 2 == 0)
    is_gt4 = (roll > 4)

    if is_even: 
        even += 1
    if is_gt4: 
        greater_than4 +=1
    if is_even or is_gt4 : 
        either += 1

P_A = even / trails
P_B = greater_than4 / trails
P_AorB = either / trails
P_AandB = (P_A + P_B) - P_AorB

print(f"P(A) = {P_A:.2f}")
print(f"P(B) = {P_B:.2f}")
print(f"P(A or B) = {P_AorB:.2f}")
print(f"P(A and B) = {P_AandB:.2f}")