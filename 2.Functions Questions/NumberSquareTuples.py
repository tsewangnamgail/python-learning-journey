start, end = map(int, input().split())
if start > end:
    print("Invalid Range")
elif start == end:
    print("Equal range")
else:
    result = []
    for i in range(start, end + 1):
        result.append((i, i * i))      #  use (,)  inside append() for list of tuples
    print(result)