# https://projecteuler.net/problem=5

x = 0

for i in range (12252240, 1000000000):
    valid = True 
    for j in range (20, 0, -1):
        if (i % j != 0):
            valid = False
            break
    
    if (valid):
        x = i
        break

print(x)