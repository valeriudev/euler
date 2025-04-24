# https://projecteuler.net/problem=3

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]

primes = get_primes(500000)

n = 600851475143
n_primes = []

quotient = n
while quotient not in primes:
    for prime in primes:
        if (quotient % prime == 0):
            n_primes.append(prime)
            quotient = int(quotient/prime)
            break

n_primes.append(quotient)

print(n_primes)

