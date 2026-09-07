from itertools import combinations

def combination_by_size(my_list, size):
    return list(combinations(my_list, size))


def all_combinations(my_list):
    for size in range(1, len(my_list) + 1):
        print(f"Size {size}:")
        print(list(combinations(my_list, size)))


my_list = [1, 2, 3, 4]
size = 2
if size:
    print(combination_by_size(my_list, size))
else:
    all_combinations(my_list)