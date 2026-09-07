# 1. POSITIONAL ARGUMENTS
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student("John", 20)


# 2. KEYWORD ARGUMENTS
def student_details(name, age):
    print("Name:", name)
    print("Age:", age)
student_details(name="John", age=20)
student_details(age=20, name="John")


# 3. DEFAULT ARGUMENTS
def greet(name="John"):
    print("Hello", name)
greet()
greet("David")


# 4. MULTIPLE ARGUMENTS
def add(a, b, c):
    print(a + b + c)
add(10, 20, 30)


# 5. *args
def total(*args):
    print(args)
    print(sum(args))
total(10, 20, 30)
total(10, 20, 30, 40, 50)


# 6. *args WITH LOOP
def numbers(*args):
    for i in args:
        print(i)
numbers(10, 20, 30, 40)


# 7. **kwargs
def details(**kwargs):
    print(kwargs)
details(name="John", age=20, course="Python")


# 8. **kwargs ACCESSING VALUES
def student_info(**kwargs):
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])
    print("Course:", kwargs["course"])
student_info(name="John", age=20, course="Python")


# 9. **kwargs WITH LOOP
def display(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
display(name="John", age=20, city="Chennai")


# 10. NORMAL ARGUMENT + DEFAULT ARGUMENT
def welcome(name, course="Python"):
    print("Name:", name)
    print("Course:", course)
welcome("John")
welcome("David", "Java")


# 11. POSITIONAL + KEYWORD ARGUMENT
def employee(name, age, city):
    print(name)
    print(age)
    print(city)
employee("John", age=20, city="Chennai")


# 12. *args + NORMAL PARAMETER
def calculate(operation, *numbers):
    print("Operation:", operation)
    print("Numbers:", numbers)
    print("Total:", sum(numbers))
calculate("Addition", 10, 20, 30, 40)


# 13. NORMAL PARAMETER + **kwargs
def person(name, **details):
    print("Name:", name)
    print("Details:", details)
person("John", age=20, city="Chennai", course="Python")


# 14. *args + **kwargs
def information(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)
information(10, 20, 30, name="John", age=20)


# 15. UNPACKING LIST USING *
numbers = [10, 20, 30]
def add(a, b, c):
    print(a + b + c)
add(*numbers)


# 16. UNPACKING DICTIONARY USING **
student = {
    "name": "John",
    "age": 20
}
def student_details(name, age):
    print("Name:", name)
    print("Age:", age)
student_details(**student)