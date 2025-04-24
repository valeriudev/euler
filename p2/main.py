# https://projecteuler.net/problem=2

x0 = 1
x1 = 1
x2 = 2
sum = 2

while x2 <= 4000000:
    x0 = x1
    x1 = x2
    x2 = x0 + x1
    if (x2 % 2 == 0):
        sum += x2
    

print(sum)
    