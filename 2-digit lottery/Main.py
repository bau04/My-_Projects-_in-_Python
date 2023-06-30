import random

print("Welcome to the 2-digit lotto draw")
print("Choose a number from 0-9")

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

x1 = int(random.randint(0,9))
x2 = int(random.randint(0,9))

if n1 == x1 & n2 == x2:
    print("\nToday's lottery result is: ")
    print("Result: You won!")
    print("Your pick: " , n1 , " , " , n2)
    print("Winning number: " , x1 , " , " , x2)

if n1 <= -1 | n2 <= -1 :
    print("Error: The number you picked is below 0")

if n1 >= 10 | n2 >= 10 :
    print("Error: The number you picked is above the range of 0-9")

elif n1 != x1 & n2 != x2:
    print("\nToday's lottery result is: ")
    print("Result: You lost")
    print("Your pick: " , n1 , " , " , n2)
    print("Winning number: " , x1 , " , " , x2)

else :
    print("\nToday's lottery result is: ")
    print("Result: lost")
    print("Your pick: " , n1 , " , " , n2)
    print("Winning number: " , x1 , " , " , x2)
