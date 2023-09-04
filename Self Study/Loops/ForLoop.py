# For Loop is used to iterate through a collection,
# or to execute a block of code in a certain amount of times
# Indentation indicates what statements are included in the loop

# For loop in collections can be used to access every item in a collection
#            x        x         x
fruits = ["apples", "mango", "orange", "grapes", "banana"]
# for every x in fruits
for x in fruits:
    print("Fruits : ", x)
else:
    print("No more fruits")  # ELSE in For loop is added to the bottom so that it can execute a code when the loop is
    # done

print(" ")

# BREAK in for loop is used to stop the loop earlier than it's supposed to finish
students = ["Boy", "Manong", "Ate", "Badot"]
for x in students:
    print("student : ", x)
    break

# You can also use any conditions in a for loop
for x in students:
    print("conditional student : ", x)
    if x == "Ate":  # code immediately stops when "Ate" is found
        break

print("")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# EVEN number divisible by 2 = r = 0
# ODD number is Not divisible by 2

for number in numbers:
    if number % 2 == 0:
        print("Number = EVEN : ", number)
    else:
        print("Number = ODD : ", number)

print("")

# Range loops a set of code in a specified number of times

for x in range(10):
    print(x)

print("")

# Nested For Loop
# using range in nested for Loop

for y in range(5):  # will loop everything inside 5x
    for z in range(5):  # this loop will be looped 5x, and it will also loop everything inside
        print("Hello")  # will be printed 25x

print("")
# "end=" is used to combine to separate printed lines into one line
print("*", end="")
print("*")  # This line will be connected to the print above

for y in range(5):  # will loop everything inside 5x
    for z in range(5):  # this loop will be looped 5x, and it will also loop everything inside
        print("*", end="")  # will be printed 25x
    print("NewLine")  # moves/prints to the next line after the "for z" loop is run

# reading multi-dimensional collections using for loop
courseStudents = [
    ["BSIT", "Bob"],
    ["BSIT", "Badot"],
    ["BSCS", "Buw"],
    ["BSCS", "Ante"],
    ["BSIT", "Manute"]
]

for listStudent in courseStudents:  # All the list inside the courseStudents list is ran
    for i in listStudent:  # loops the nested list individually
        print(i)  # prints the item of the nested list individually
    print()  # Creates a space everytime the loop completed a cycle
