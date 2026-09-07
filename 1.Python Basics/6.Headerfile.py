# 1. MATH
import math
a = 12
b = 18
print("GCD / HCF:", math.gcd(a, b))
print("LCM:", math.lcm(a, b))
print("Square root:", math.sqrt(25))
print("Factorial:", math.factorial(5))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.8))

#lcm and gcd of list
lst=list(map(int,input().split()))
print(math.lcm(*lst))
print(math.gcd(*lst))




# 2. COLLECTIONS
from collections import Counter, deque, defaultdict

# Counter
c = Counter([1, 2, 2, 3, 3, 3])
print(c)
print(c[3])                  # 3
print(c.most_common())       # [(3, 3), (2, 2), (1, 1)]
print(c.most_common(2))      # top 2

# deque
q = deque()
q.append(10)
q.append(20)
q.appendleft(5)
print(q)                     # deque([5, 10, 20])
print(q.popleft())           # 5
print(q.pop())               # 20

# defaultdict
d = defaultdict(int)
d["apple"] += 1
d["apple"] += 1
d["banana"] += 1
print(d)                     # {'apple': 2, 'banana': 1}



# 3. HEAPQ
import heapq
h = [5, 2, 8, 1, 10]
heapq.heapify(h)
print(h)
heapq.heappush(h, 0)
print(h)
print(heapq.heappop(h))      # smallest element
print(heapq.nsmallest(2, h))
print(heapq.nlargest(2, h))



# 4. BISECT
import bisect
arr = [10, 20, 30, 40, 50]
print(bisect.bisect_left(arr, 30))   # 2
print(bisect.bisect_right(arr, 30))  # 3
bisect.insort(arr, 25)
print(arr)                   # [10, 20, 25, 30, 40, 50]



# 5. ITERTOOLS
from itertools import permutations, combinations, product, accumulate
arr = [1, 2, 3]
# Permutations
print(list(permutations(arr)))
# Combinations
print(list(combinations(arr, 2)))
# Product
print(list(product([1, 2], [3, 4])))
# Accumulate
print(list(accumulate([1, 2, 3, 4])))
# [1, 3, 6, 10]



# 6. FUNCTOOLS
from functools import reduce, cache

numbers = [1, 2, 3, 4]
# reduce
result = reduce(lambda x, y: x + y, numbers)
print(result)                # 10

# cache - useful in recursion / DP
@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(10))               # 55



# 7. SYS
import sys
# Fast input
# n = int(sys.stdin.readline())
# Read everything
# data = sys.stdin.read()
# Fast output
# sys.stdout.write("Hello\n")
print("sys module loaded")



# 8. STRING
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.ascii_letters)
print(string.punctuation)



# 9. REGEX
import re
text = "My marks are 90 and 85"
print(re.findall(r'\d+', text))
# ['90', '85']
print(re.search(r'\d+', text))
print(re.sub(r'\d+', '100', text))
# My marks are 100 and 100



# 10. RANDOM
import random
print(random.randint(1, 10))
print(random.choice([10, 20, 30]))
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)


# 11. OPERATOR
import operator
print(operator.add(10, 20))       # 30
print(operator.sub(20, 10))       # 10
print(operator.mul(5, 4))         # 20
print(operator.gt(10, 5))         # True
print(operator.lt(10, 5))         # False
print(operator.eq(10, 10))        # True