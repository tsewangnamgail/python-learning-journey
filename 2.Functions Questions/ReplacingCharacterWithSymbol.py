s = input("Enter string: ")

n = int(input("Enter number of replacements: "))

for _ in range(n):
    old = input("Character to replace: ")
    new = input("Replacement character: ")

    s = s.replace(old, new)

print(s)