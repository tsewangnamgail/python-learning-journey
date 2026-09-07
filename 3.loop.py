# PYTHON LOOPS

# 1. FOR LOOP
for i in range(5):
    print(i,end=" ")    # 0 1 2 3 4

# 2. RANGE WITH START AND STOP
for i in range(1, 6):
    print(i,end=" ")  # 1 2 3 4 5

# 3. RANGE WITH START, STOP AND STEP
for i in range(1, 10, 2):
    print(i,end=" ")   # 1 3 5 7 9

# 4. REVERSE LOOP
for i in range(5, 0, -1):
    print(i,end=" ")  # 5 4 3 2 1

# 5. LOOP THROUGH STRING
name = "Python"
for char in name:
    print(char,end=" ") # P y t h o n

# 6. LOOP THROUGH LIST
numbers = [10, 20, 30, 40]
for number in numbers:
    print(number,end=" ")  # 10 20 30 40

# 7. LOOP THROUGH TUPLE
numbers = (10, 20, 30, 40)
for number in numbers:
    print(number,end=" ") # 10 20 30 40


# 8. LOOP THROUGH SET
numbers = {10, 20, 30, 40}
for number in numbers:
    print(number,end=" ")   # 10 20 30 40


# 9. LOOP THROUGH DICTIONARY KEYS
student = {
    "name": "Tsewang",
    "age": 21,
    "marks": 90
}
for key in student:
    print(key)  #name age marks


# 10. LOOP THROUGH DICTIONARY VALUES
for key in student:
    print(student[key])  # Tsewang 21 90


# 11. LOOP THROUGH DICTIONARY KEY AND VALUE
for key, value in student.items():
    print(key, value)  #name Tsewang, age 21, marks 90


# 12. WHILE LOOP
i = 1
while i <= 5:
    print(i)
    i += 1    #1 2 3 4 5


# 13. WHILE LOOP WITH USER INPUT
number = int(input("Enter a number: "))
i = 1
while i <= number:
    print(i)
    i += 1   #1 2 3 4 5


# 14. BREAK
for i in range(1, 10):
    if i == 5:
        break
    print(i)   #1 2 3 4 


# 15. CONTINUE
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # 1 2 4 5 6


# 16. PASS
for i in range(5):
    pass    #nothing


# 17. NESTED FOR LOOP
for i in range(3):
    for j in range(2):
        print(i, j)


# 18. NESTED LOOP WITH NUMBERS
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# 19. FOR LOOP WITH ELSE
for i in range(5):
    print(i)
else:
    print("Loop completed")


# 20. WHILE LOOP WITH ELSE
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed")


# 21. PRINT NUMBERS 1 TO 10
for i in range(1, 11):
    print(i)


# 22. PRINT EVEN NUMBERS
for i in range(2, 11, 2):
    print(i)


# 23. PRINT ODD NUMBERS
for i in range(1, 11, 2):
    print(i)


# 24. SUM OF NUMBERS
total = 0
for i in range(1, 6):
    total += i
print(total)


# 25. MULTIPLICATION TABLE
number = 5
for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 26. REVERSE NUMBERS
for i in range(10, 0, -1):
    print(i)


# 27. LOOP THROUGH LIST WITH INDEX
numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    print(i, numbers[i])


# 28. NESTED LIST
numbers = [
    [1, 2, 3],
    [4, 5, 6]
]
for row in numbers:
    for number in row:
        print(number)


# 29. BREAK IN WHILE LOOP
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1


# 30. CONTINUE IN WHILE LOOP
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)