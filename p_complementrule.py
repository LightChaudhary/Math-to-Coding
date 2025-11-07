import random 

trail = 10000
heads = 0

for _ in range(trail) :
    toss = random.choice(["H", "T"])
    if toss == "H": 
        heads += 1

p_heads = heads / trail
p_tails = 1 - p_heads

print("The possibilities of outcome heads: ", p_heads)
print("The possibilities of outcome tails: ", p_tails)