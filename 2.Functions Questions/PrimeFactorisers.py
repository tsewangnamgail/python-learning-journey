import math

def prime_factors(n):
    factors = []

    for i in range(2, math.isqrt(n) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 1:
        factors.append(n)

    return factors


n = int(input())
print(prime_factors(n))