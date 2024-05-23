# --- Variables and Data Types

# Variables
x = 10            # Integer
y = 3.14          # Float
name = "Alice"    # String

# Data Types
# List
fruits = ["apple", "banana", "cherry"]

# Tuple
coordinates = (10.0, 20.0)

# Dictionary
person = {"name": "Alice", "age": 25}



# --- Basic Operations

# Arithmetic
addition = 5 + 3         # 8
subtraction = 5 - 3      # 2
multiplication = 5 * 3   # 15
division = 5 / 3         # 1.6667

# Comparison
is_equal = 5 == 3        # False
not_equal = 5 != 3       # True
greater_than = 5 > 3     # True

# Logical
and_operation = True and False  # False
or_operation = True or False    # True
not_operation = not True        # False



# --- Control Structures

# If-Else Statement
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")



# --- Loop

# For Loop
for i in range(5):
    print(i)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1



# --- Functions 

# Define a function that greets a person by name
def greet(name):
    print("Hello, " + name)

greet("Alice")

# Define a function that adds two numbers
def add(a, b):
    return a + b

# Call the add function and print the result
total = add(3, 5)
print(total)  


# Built-in Functions
print("Hello, World!")            # Prints Hello, World!
user_input = input("Enter something: ")
length = len("Python")            # 6

# Using Libraries
import random
random_number = random.randint(1, 10)  # Random number between 1 and 10

import math
square_root = math.sqrt(16)            # 4.0
