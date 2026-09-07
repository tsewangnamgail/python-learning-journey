# 1. DEFINING A FUNCTION
def greet():
    print("Hello")
greet()  #fucntion calling


# 3. FUNCTION WITHOUT PARAMETERS
def welcome():
    print("Welcome to Python")
welcome()


# 4. PARAMETERS AND ARGUMENTS
def greet_person(name):
    print("Hello", name)
greet_person("John")


# 5. MULTIPLE PARAMETERS
def add(a, b):
    print(a + b)
add(10, 20)


# 6. MULTIPLE PARAMETERS WITH DIFFERENT VALUES
def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
student("John", 20, "Python")


# 7. RETURN
def addition(a, b):
    return a + b
result = addition(10, 20)
print(result)


# 8. RETURN WITH MULTIPLICATION
def multiply(a, b):
    return a * b
result = multiply(5, 4)
print(result)


# 9. FUNCTION WITHOUT RETURN VALUE
def display_sum(a, b):
    print(a + b)
display_sum(10, 20)


# 10. FUNCTION WITH RETURN VALUE
def calculate_sum(a, b):
    return a + b
x = calculate_sum(10, 20)
print(x)


# 11. USING RETURN VALUE IN ANOTHER CALCULATION
def square(n):
    return n * n
result = square(5)
print(result)
answer = result + 10
print(answer)


# 12. LOCAL VARIABLE
def local_example():
    x = 10
    print(x)
local_example()   #10


# 13. GLOBAL VARIABLE
x = 100
def global_example():
    print(x)
global_example()


# 14. GLOBAL AND LOCAL VARIABLE
x = 100
def example():
    x = 50
    print(x) #50
example()
print(x)     #100


# 15. FUNCTION USING GLOBAL VARIABLE
name = "John"
def show_name():
    print(name)
show_name()


# 16. SAME FUNCTION CALLED MULTIPLE TIMES
def greet(name):
    print("Hello", name)
greet("John")
greet("David")
greet("Alice")


# 17. FUNCTION WITH THREE PARAMETERS
def total(a, b, c):
    return a + b + c
result = total(10, 20, 30)
print(result)


# 18. FUNCTION WITH FOUR PARAMETERS
def calculate(a, b, c, d):
    return a + b + c + d
result = calculate(10, 20, 30, 40)
print(result)


# 19. FUNCTION TAKING INPUT
def user_details(name, age):
    print("Name:", name)
    print("Age:", age)
name = input("Enter name: ")
age = int(input("Enter age: "))
user_details(name, age)


# 20. FUNCTION RETURNING MULTIPLE VALUES
def operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication
x, y, z = operations(10, 5)
print(x)
print(y)
print(z)