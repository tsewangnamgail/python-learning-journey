# IF ELSE BASICS

# 1. IF
age = 20
if age >= 18:
    print("Adult")

# 2. IF ELSE
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 3. IF ELIF ELSE
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 4. COMPARISON OPERATORS
a = 10
b = 20
if a == b:
    print("Equal")
if a != b:
    print("Not equal")
if a > b:
    print("a is greater")
if a < b:
    print("a is smaller")
if a >= b:
    print("a is greater or equal")
if a <= b:
    print("a is smaller or equal")

# 5. AND OPERATOR
age = 20
marks = 80
if age >= 18 and marks >= 50:
    print("Eligible")

# 6. OR OPERATOR
age = 17
if age >= 18 or age == 17:
    print("Allowed")

# 7. NOT OPERATOR
is_student = False
if not is_student:
    print("Not a student")


# 8. NESTED IF
age = 20
marks = 80
if age >= 18:
    if marks >= 50:
        print("Eligible")

# 9. USER INPUT
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# 10. USER INPUT WITH ELIF
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")

# 11. MULTIPLE CONDITIONS
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

# 12. EVEN OR ODD
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 13. POSITIVE, NEGATIVE OR ZERO
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 14. LARGEST OF TWO NUMBERS
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("a is largest")
elif b > a:
    print("b is largest")
else:
    print("Both are equal")

# 15. LARGEST OF THREE NUMBERS
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
elif c > a and c > b:
    print("c is largest")
else:
    print("Some numbers are equal")