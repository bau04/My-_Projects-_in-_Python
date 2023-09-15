# lambda is a small anonymous function that can take any amount of arguments but can only have ONE expression

add = lambda x, y: x + y
print(add(2, 3))

print()

subtract = lambda n, m: n - m
print(subtract(10, 4))

print()

# Assignment
# Create a lambda function that takes one argument and triples the argument passed in it

# longer version

tripler = lambda b: b * 3
num = int(input("Enter the number you want to triple: "))  # gets input and convert it to integer
print(tripler(num))  # prints the tripler with num

# short version:

triple = lambda a: a * 3
print(triple(int(input("Enter the number you want to triple: "))))
# prints user input that is cast into integer which also gave the triple valuable "a" its value
