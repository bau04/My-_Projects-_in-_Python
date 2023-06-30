import random

print("Welcome to the 6-digit lottery draw")
print("Choose a number from 0-9")

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))
n5 = int(input("Enter fifth number: "))
n6 = int(input("Enter sixth number: "))

x1 = int(random.randint(0,9))
x2 = int(random.randint(0,9))
x3 = int(random.randint(0,9))
x4 = int(random.randint(0,9))
x5 = int(random.randint(0,9))
x6 = int(random.randint(0,9))

if n1 == x1 and n2 == x2 and n3 == x3 and n4 == x4 and n5 == x5 and n6 == x6:
    print("\nToday's lottery result is: ")
    print("Winning number: " , x1 , " , " , x2 , " , " , x3 , " , " , x4 , " , " , x5 , " , " , x6)
    print("     Your pick: " , n1 , " , " , n2 , " , " , n3 , " , " , n4 , " , " , n5 , " , " , n6)
    print("        Result: You Won!!!")

elif n1 <= -1 or n2 <= -1 or n3 <= -1 or n4 <= -1 or n5 <= -1 or n6 <= -1 :
    print("Error: The number you picked is below the range")

elif n1 >= 10 or n2 >= 10 or n3 >= 10 or n4 >= 10 or n5 >= 10 or n6 >= 10 :
    print("Error: The number you picked is above the range ")

elif n1 != x1 or n2 != x2 or n3 != x3 or n4 != x4 or n5 != x5 or n6 != x6:
    print("\nToday's lottery result is: ")
    print("Winning number: " , x1 , " , " , x2 , " , " , x3 , " , " , x4 , " , " , x5 , " , " , x6)
    print("     Your pick: " , n1 , " , " , n2 , " , " , n3 , " , " , n4 , " , " , n5 , " , " , n6)
    print("        Result: You lost")
