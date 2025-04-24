# https://projecteuler.net/problem=6

x = 0
y = 0

for i in range (1, 101):
    x += i*i 
    y += i

y *= y

print(x, y, y-x)