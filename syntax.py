x = 5
y = "hello"
z = 3.14
#  check the types of the variables
print(type(x))
print(type(y))
print(type(z))
print("-------------------------------------------------")  
# dynamic typing: the same variable can hold different types over time
x = 10
print(type(x))  # int

x = "hello"
print(type(x))  # str

x = [1, 2, 3]
print(type(x))  # list
print("-------------------------------------------------")  
movies = ["Arrival", "Interstellar", "Dune"]  # list
point = (4, 9)                                # tuple
grades = {"Alice": 95, "Bob": 87} 
# accessing and modifying a list:
print(movies[0])  # "Arrival"
movies.append("The Martian")
print(movies)  # ["Arrival", "Interstellar", "Dune", "The Martian"]
# accessing a tuple:
print(point[0])  # 4
# accessing and modifying a dictionary:
print(grades["Alice"])  # 95
grades["Charlie"] = 92
print(grades)  # {"Alice": 95, "Bob": 87, "Charlie": 92}\print("-------------------------------------------------")  
print("-------------------------------------------------")  

# Conditionals
score = 72
if score >= 90:
    print("A")
elif score >= 80:
   print("B")
else:
    print("Keep going!")

# check if a number is negative, positive, or zero
num = -7
if num < 0:
    print("Negative")
elif num > 0:
    print("Positive")
else:
    print("Zero")
print("-------------------------------------------------")

# Loops
# loop using range()
for i in range(5):
    print(i)  # prints 0, 1, 2, 3, 4
# while loop:
i = 1
while i <= 5:
    print(i)  # prints 1, 2, 3, 4, 5
    i += 1
print("-------------------------------------------------")

# Exceptions
# a program asks the user for a number to divide by.
# without exception handling, bad input (like "0" or "abc") would crash the program.
try:
    user_input = input("Enter a number to divide 100 by: ")
    divisor = int(user_input)       # could raise ValueError if input isn't a number
    result = 100 / divisor          # could raise ZeroDivisionError if divisor is 0
    print(f"100 / {divisor} = {result}")
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero.")

# simple snippet that just catches a divide-by-zero error
try:
    answer = 10 / 0   # this line raises ZeroDivisionError
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
print("-------------------------------------------------")

# Modules
# import built-in modules to extend what Python can do
import math
import random

print(math.sqrt(16))      # square root -> 4.0
print(random.randint(1, 10))  # random int between 1 and 10 (inclusive)

# modules and a simple example for each:
# 1. math    - math operations          -> math.sqrt(16) -> 4.0
# 2. random  - random numbers/choices   -> random.choice(["a", "b", "c"])
# 3. datetime- dates and times          -> datetime.date.today()
# 4. os      - interact with the OS     -> os.getcwd()
# 5. statistics - basic stats functions -> statistics.mean([1, 2, 3])

# print a random number between 1 and 50
print(random.randint(1, 50))
print("-------------------------------------------------")
