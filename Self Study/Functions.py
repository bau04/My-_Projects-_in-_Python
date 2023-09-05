# Functions are used to organize and divide specific tasks in a program that will only run when it is called
# Indentation is used to indicate what statements are included inside the function

# Creating Functions
# "def function_Name():
#       Do Something

def sayHello():
    print("Hello")

# to call functions, just type the function_name()
sayHello()

# Arguments and parameters are values passed inside a function that will be used to perform tasks
# "def function_Name(parameters):
#       Do Something
# to call functions, just type the function_name()


def sayName(firstName, lastName):
    print("Hello!", firstName, lastName)

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
sayName(firstname, lastname)

print("")
# return values are returned by a function once it is finished executing.
# it returns results from a function that computes or does something that needs a result

# "def function_Name(parameters):
#       return value
# function_name(parameter)

n1 = int(input("Enter First Number"))
n2 = int(input("Enter Second Number"))

def addNumbers(num1, num2):
    return num1 + num2

sum = addNumbers(n1, n2)

print(sum)
