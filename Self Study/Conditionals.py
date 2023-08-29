# IF statements (1 condition)
# IF-ELSE statements (2 conditions)
# IF-ELIF-ELSE statements (3 or more conditions)
# NESTED statements (Condition after a condition)

height = int(input("Enter your height in cm : "))

if height > 180 :
    print("You are tall")  # the "If" is the first condition

elif 170 < height :
    print("Your height is average")  # the "Elif" is used to add more conditions if the first is not met

else :
    print("You are short")  # "Else" is used if none of the conditions apply

print(" ")

# if "not" value1 == value2: inverts the condition value

# Logical Operators
# "and" BOTH conditions must be true
# "or" EITHER of the conditions must be true

# If statement with lists
bag = ["Keys", "Gun", "Perfume", "Charger", "Laptop"]

if "Gun" in bag :
    print("You are busted")

else:
    print("You can go through")

print(" ")

# Grade Average Program

gradeOne = int(input("Enter first grade : "))
gradeTwo = int(input("Enter second grade : "))
gradeThree = int(input("Enter third grade : "))

Average = ((gradeOne + gradeTwo + gradeThree) / 3)

if Average > 100 or Average < 50 :
    print("Invalid Grade")

elif Average >= 98 :
    print("Average Grade : ", Average, ": With Highest Honor")

elif Average >= 95:
    print("Average Grade : ", Average, ": With High Honor")

elif Average >= 90:
    print("Average Grade : ", Average, ": With Honor")

elif Average >= 75:
    print("Average Grade : ", Average, ": Passed")

else:
    print("Average Grade : ", Average, ": Failed")
