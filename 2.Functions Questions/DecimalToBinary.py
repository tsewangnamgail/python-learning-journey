n = float(input())

integer = int(n)
fraction = n - integer

# Integer part
binary = bin(integer)[2:]

# Fractional part
if fraction != 0:
    binary += "."

    while fraction > 0:
        fraction *= 2

        if fraction >= 1:
            binary += "1"
            fraction -= 1
        else:
            binary += "0"

print(binary)