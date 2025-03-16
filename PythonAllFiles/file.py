# Python Basics Analyzer
import sys

print("🚀 Welcome to Python Analysis Script 🚀\n")
print("Python Version:", sys.version, "\n")

# ---------------- 1. VARIABLES & DATA TYPES ----------------
x = 10       # Integer
y = 20.5     # Float
z = "Hello"  # String
lst = [1, 2, 3]  # List
tpl = (4, 5, 6)  # Tuple
st = {7, 8, 9}   # Set
dct = {"a": 1, "b": 2}  # Dictionary

print("✅ Variables & Data Types: ", type(x), type(y), type(z), type(lst), type(tpl), type(st), type(dct), "\n")

# ---------------- 2. CONDITIONAL STATEMENTS ----------------
num = 15
if num > 10:
    print("✅ If-Else Condition: Number is greater than 10\n")
else:
    print("Number is 10 or less\n")

# ---------------- 3. LOOPS ----------------
print("✅ Loop Examples:")
for i in range(3):
    print(f"For Loop Iteration {i}")

count = 0
while count < 3:
    print(f"While Loop Iteration {count}")
    count += 1
print("")

# ---------------- 4. FUNCTIONS ----------------
def greet(name):
    return f"Hello, {name}!"

print("✅ Function Output:", greet("Suryansh"), "\n")

# ---------------- 5. EXCEPTION HANDLING ----------------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("✅ Exception Handling: Division by zero is not allowed!\n")

# ---------------- 6. FILE HANDLING ----------------
with open("sample.txt", "w") as f:
    f.write("Hello, this is a test file.")

with open("sample.txt", "r") as f:
    print("✅ File Handling:", f.read(), "\n")

# ---------------- 7. CLASSES & OBJECTS ----------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def details(self):
        return f"{self.brand} - {self.model}"

my_car = Car("Tesla", "Model S")
print("✅ Object-Oriented Programming:", my_car.details(), "\n")

# ---------------- 8. LAMBDA FUNCTION ----------------
square = lambda x: x**2
print("✅ Lambda Function (Square of 5):", square(5), "\n")

# ---------------- 9. LIST COMPREHENSION ----------------
nums = [x for x in range(5)]
print("✅ List Comprehension:", nums, "\n")

# ---------------- 10. IMPORTING MODULES ----------------
import math
print("✅ Math Module (Square Root of 25):", math.sqrt(25), "\n")

# ---------------- 11. USER INPUT ----------------
# Uncomment the below lines to take input
# user_name = input("Enter your name: ")
# print(f"✅ User Input: Hello, {user_name}!\n")

# ---------------- END ----------------
print("✅ Python Analysis Complete ✅")