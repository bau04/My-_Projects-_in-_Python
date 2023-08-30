# Indentation is used to indicate what statements are inside the loop
# While Loop will repeat a block of code until condition is fulfilled

age = 11

while age < 18 :  # while loop with its condition
    print("You are a minor", str(age))
    age = age + 1  # the increment to add 1 value
else:  # Else ran for 1 time in while loop
    print("You are OLD", str(age))

print(" ")

# While loop can be used to access every item in collections...
# (Lists and tuples) since it is indexed and ordered

# INDEX         0       1      2       3
studentID = [202300, 202301, 202302, 202304]
i = 0

while i <= 3 :  # this loop is used access the values individually without brackets
    print(studentID[i])
    i = i + 1

print(" ")

# INDEX         0       1      2       3        4
studentIDs = [202300, 202301, 202302, 202304, 202305]
i = 0

# VERSION 2 where the condition includes the whole length of the list
while i < len(studentIDs) :  # this loop is used access the values individually without brackets
    print(studentIDs[i])
    i = i + 1

print(" ")

# Conditionals in while loop can use any conditional statement inside the loop
# "Break" is used to stop the loop no matter what the condition is

print("Does your crush like you back? ")

while True :  # this loop continue to loop when the answer is yes
    answer = input("Answer: ")
    if answer == "no" :
        print("Correct! ")
        break
    else :
        print("You are wrong")

print(" ")

# sorting the values of a lists whether it's even or odd number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

while i < len(numbers) :
    if numbers[i] % 2 == 0:
        print("Even Number : ", numbers[i])
    else :
        print("Odd Number : ", numbers[i])
    i = i + 1
