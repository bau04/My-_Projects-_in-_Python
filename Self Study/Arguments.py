# Arguments or parameters are values passed inside a function that will be used to perform tasks

def sayHi(name):
    print("Hi", name)

sayHi(input("enter your name: "))

print("")

# Arbitrary Arguments "(*args)" are used if you don't exactly know how many arguments is needed in your function
# Arbitrary Arguments passed in will be considered as a tuple allowing it to be iterated using a loop
# Arbitrary arguments = infinite amount of arguments

def sayHello(*nombre):
    print("Hello", nombre)

sayHello("Charles", "Caroline", "Chase", "Camilla", "Coco")

# with loop

def sayHola(*nombres):
    for nombre in nombres:
        print("Hola", nombre)

sayHola("Charles", "Caroline", "Chase", "Camilla", "Coco")  # will be printed individually

print()

# keyword arguments (kwargs) alternative way to send arguments to a function
# often used in combination with arbitrary arguments
# kwargs specify parameter name in no certain order

def printFamily(*firstName, lastName):
    for name in firstName:
        print(name, lastName)

printFamily("Marc", "Martel", "Luigi", lastName="Moreno")  # firstname is arbitrary and lastname is specified

# two arbitrary arguments (*args) are also not allowed in a single function

# arbitrary keyword arguments (**kwargs) are used when you are uncertain on what parameter name you want to pass
def printStudent(**student):
    print(student["name"])  # keyword should always be a string ["name"]
    print(student["age"])
    print(student["course"])

printStudent(name="Bitoy", age=19, course="BSIT")
