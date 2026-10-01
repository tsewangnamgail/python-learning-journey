from itertools import combinations   #remember the file header


def combination_by_size(my_list, size):         #list(combinations(user_list,size))
    return list(combinations(my_list, size))     #find all the combination with size


def all_combinations(my_list):   
    for size in range(1, len(my_list) + 1):      #iteration through all the size
        print(f"Size {size}:")
        print(list(combinations(my_list, size)))


user_input = input("Enter elements separated by space: ")
my_list = user_input.split()
size = int(input("Enter combination size (0 for all combinations): "))

if size:
    print(combination_by_size(my_list, size))
else:
    all_combinations(my_list)