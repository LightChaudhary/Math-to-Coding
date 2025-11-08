import random 

deck = ["Ace"] * 4 + ["Other"] * 48
trails = 10000
both_aces = 0

for _ in range(trails): 
    draw = random.sample(deck, 2)
    
    if draw[0] == "Ace" and draw[1] == "Ace": 
        both_aces += 1

P_AandB = both_aces / trails
print(f"The probability of getting both aces: {P_AandB:.4f} ")