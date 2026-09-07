# PYTHON BASICS


# 1. PRINT
print("Hello, Python!")
print(10)
print(10 + 20)
print("My name is Tsewang")


# 2. COMMENTS
# This is a single-line comment
"""
This is a
multi-line comment
"""


# 3. VARIABLES
name = "Tsewang"
age = 21
height = 5.8
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# 4. MULTIPLE VARIABLES
x = 10
y = 20
z = 30
print(x, y, z)
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
p = q = r = 100
print(p, q, r)


# 5. DATA TYPES
integer_value = 10
float_value = 10.5
string_value = "Python"
boolean_value = True
complex_value = 2 + 3j
print(type(integer_value))
print(type(float_value))
print(type(string_value))
print(type(boolean_value))
print(type(complex_value))


# 6. INTEGER
age = 21
marks = 95
print(age)
print(marks)
print(type(age))


# 7. FLOAT
price = 99.99
percentage = 85.5
print(price)
print(percentage)
print(type(price))
x = 10.5678  #rounding off
print(round(x, 2))


# 8. STRING
name = "Tsewang"
print(name)
print(type(name))

city = 'Chennai'
country = "India"
print(city)
print(country)


# 9. BOOLEAN
is_active = True
is_logged_in = False
print(is_active)
print(is_logged_in)
print(type(is_active))


# 10. TYPE CONVERSION
x = "100"
x = int(x)
print(x)
print(type(x))

x = "10.5"
x = float(x)
print(x)
print(type(x))

x = 10
x = float(x)
print(x)

x = 100
x = str(x)
print(x)
print(type(x))

x = 10.99
x = int(x)
print(x)


# 11. INPUT
name = input("Enter your name: ")
print("Your name is", name)
age = int(input("Enter your age: "))
print("Your age is", age)
height = float(input("Enter your height: "))
print("Your height is", height)
# multiple input in single line
a, b, c = map(int, input().split()) #map()
print(a)
print(b)
print(c)


# 12. ARITHMETIC OPERATORS
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)  #ip:(10/2)  op:5.0 (float)
print(a // b) #ip:(20/6)  op:3 (int)
print(a % b)
print(a ** b)


# 13. ASSIGNMENT OPERATORS
x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 2
print(x)

x //= 2
print(x)

x %= 3
print(x)

x **= 2
print(x)


# 14. COMPARISON OPERATORS

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# 15. LOGICAL OPERATORS

x = True
y = False

print(x and y)
print(x or y)
print(not x)


# 16. IDENTITY OPERATORS

a = 10
b = 10

print(a is b)    #True
print(a is not b)  #False


# 17. MEMBERSHIP OPERATORS

name = "Python"

print("P" in name)      #True
print("z" in name)      #False
print("P" not in name)  #False


# 18. STRING BASICS

text = "Python Programming"

print(text)
print(len(text))


# 19. STRING INDEXING

text = "Python"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

print(text[-1])
print(text[-2])


# 20. STRING SLICING

text = "Python"

print(text[0:3])    #(start:end:step)
print(text[1:4])
print(text[:3])
print(text[3:])
print(text[:])
print(text[::-1])


# 21. STRING CONCATENATION

first_name = "Tsewang"
last_name = "Namgail"

full_name = first_name + " " + last_name

print(full_name)


# 22. STRING REPETITION

text = "Python "

print(text * 3)


# 23. STRING METHODS

text = "python programming"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

text = "   Python   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

text = "I like Java"
print(text.replace("Java", "Python"))

text = "banana"
print(text.count("a"))

text = "Python Programming"
print(text.find("Python"))
print(text.find("Programming"))
print(text.startswith("Python"))
print(text.endswith("ing"))

text = "Python is easy"
words = text.split()
print(words)   #['Python', 'is', 'easy']
words = ["Python", "is", "easy"]
sentence = " ".join(words)
print(sentence)

a = "12345"
print(a.isdigit())  #true
a = "Python"
print(a.isalpha())  #true
a = "Python123"
print(a.isalnum())  #true


# 24. LIST   List → Mutable, ordered collection that allows duplicates.
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[-1])


# 25. LIST SLICING
numbers = [10, 20, 30, 40, 50]
print(numbers[0:3])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])
print(numbers[::-1])


# 26. LIST METHODS
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)  #[10, 20, 30, 40]
numbers.insert(1, 15)  #(index,value)
print(numbers)   #[10, 15, 20, 30, 40]
numbers.remove(15)
print(numbers)   #[10, 20, 30, 40]
numbers.pop()
print(numbers)   #[10, 20, 30]
numbers = [40, 10, 30, 20]
numbers.sort() 
print(numbers) #[10, 20, 30, 40]
numbers.reverse()
print(numbers)   #[40, 30, 20, 10]
print(len(numbers))  #4


# 27. LIST WITH DIFFERENT DATA TYPES
student = ["Tsewang", 21, 85.5, True]
print(student)
print(student[0])
print(student[1])
print(student[2])
print(student[3])


# 28. TUPLE  Immutable, ordered collection that allows duplicates.
numbers = (10, 20, 30, 40)
print(numbers)
print(numbers[0])
print(numbers[-1])
print(len(numbers))
print(numbers[1:3])


# 29. SET  Mutable, unordered collection that does not allow duplicates.
numbers = {10, 20, 30, 20, 10}
print(numbers)
numbers.add(40)
print(numbers)
numbers.remove(20)
print(numbers)
print(len(numbers))


# 30. DICTIONARY
student = {
    "name": "Tsewang",
    "age": 21,
    "marks": 85
}
print(student)
print(student["name"])
print(student["age"])
print(student["marks"])


# 31. ADD / MODIFY DICTIONARY VALUES
student["city"] = "Chennai"
print(student)
student["marks"] = 95
print(student)


# 32. DICTIONARY METHODS
student = {
    "name": "Tsewang",
    "age": 21,
    "marks": 95
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.get("age"))


# 33. NESTED LIST
numbers = [
    [1, 2, 3],
    [4, 5, 6]
]
print(numbers)
print(numbers[0])
print(numbers[0][0])
print(numbers[1][2])


# 34. NESTED DICTIONARY
students = {
    "student1": {
        "name": "Tsewang",
        "age": 21
    },
    "student2": {
        "name": "Rahul",
        "age": 22
    }
}
print(students)
print(students["student1"]["name"])
print(students["student2"]["age"])


# 35. F-STRING
name = "Tsewang"
age = 21
print(f"My name is {name}")
print(f"I am {age} years old")
marks = 95
print(f"My name is {name}, I am {age} years old and my marks are {marks}")


# 36. ESCAPE CHARACTERS
print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Python is easy\"")


# 37. BASIC BUILT-IN FUNCTIONS
numbers = [10, 20, 30, 40, 50]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

x = -10
print(abs(x))

x = 10.5678
print(round(x))
print(round(x, 2))


# 38. OPERATOR PRECEDENCE
result = 10 + 5 * 2
print(result)
result = (10 + 5) * 2
print(result)

# 39. SWAPPING VARIABLES
a = 10
b = 20
a, b = b, a
print(a)
print(b)


# 40. CHECKING DATA TYPES
x = 10
y = 10.5
z = "Python"
a = True
b = [1, 2, 3]
c = (1, 2, 3)
d = {1, 2, 3}
e = {"name": "Tsewang"}

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))