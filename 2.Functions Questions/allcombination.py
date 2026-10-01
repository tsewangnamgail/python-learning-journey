from itertools import combinations

s = input("Enter string: ")
arr = list(s)

for r in range(len(arr), -1, -1):
    for combo in combinations(arr, r):
        print(list(combo), end=" ")