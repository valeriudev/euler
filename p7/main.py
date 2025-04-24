# https://projecteuler.net/problem=7

import math

primes_count = 1
lookup = 0

def is_prime(n):
    for j in range (3, int(math.sqrt(n))+1):
        if (n % j == 0):
            return False
    return True

for i in range(3, 500000000, 2):
    if (is_prime(i)):
        primes_count += 1
    if (primes_count >= 10001):
        lookup = i
        break

print(primes_count, lookup)
