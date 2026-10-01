import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):   # check till isqrt(n)+1
        if n % i == 0:
            return False
    return True


def is_circular_prime(n):
    s = str(n)                  #type conversion
    for i in range(len(s)):
        rotated = int(s[i:] + s[:i])     #rotation of number(string format)
        if not is_prime(rotated):  
            return False
    return True


n = int(input())
if is_circular_prime(n):
    print("Circular Prime")
else:
    print("Not Circular Prime")