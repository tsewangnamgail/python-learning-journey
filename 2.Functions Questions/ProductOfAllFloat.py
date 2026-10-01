s = input()

numbers = s.split(",")

product = 1

for num in numbers:
    product *= float(num)

print(product)