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

if n1 == x1 & n2 == x2 & n3 == x3 & n4 == x4 & n5 == x5 & n6 == x6:
    print("\nToday's lottery result is: ")
    print("Winning number: " , x1 , " , " , x2 , " , " , x3 , " , " , x4 , " , " , x5 , " , " , x6)
    print("     Your pick: " , n1 , " , " , n2 , " , " , n3 , " , " , n4 , " , " , n5 , " , " , n6)
    print("        Result: You Won!!!")

if n1 <= -1 | n2 <= -1 | n3 <= -1 | n4 <= -1 | n5 <= -1 | n6 <= -1 :
    print("Error: The number you picked is below the range")

if n1 >= 10 | n2 >= 10 | n3 >= 10 | n4 >= 10 | n5 >= 10 | n6 >= 10 :
    print("Error: The number you picked is above the range ")

elif n1 != x1 & n2 != x2 & n3 != x3 & n4 != x4 & n5 != x5 & n6 != x6:
    print("\nToday's lottery result is: ")
    print("Winning number: " , x1 , " , " , x2 , " , " , x3 , " , " , x4 , " , " , x5 , " , " , x6)
    print("     Your pick: " , n1 , " , " , n2 , " , " , n3 , " , " , n4 , " , " , n5 , " , " , n6)
    print("        Result: You lost")

else :
    print("\nToday's lottery result is: ")
    print("Winning number: " , x1 , " , " , x2 , " , " , x3 , " , " , x4 , " , " , x5 , " , " , x6)
    print("     Your pick: " , n1 , " , " , n2 , " , " , n3 , " , " , n4 , " , " , n5 , " , " , n6)
    print("        Result: You lost")
