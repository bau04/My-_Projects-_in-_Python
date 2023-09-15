# create a function that will accept N number of integers as arguments
# it should get the sum of all integers passed into the function and return its sum

def summationOf(*numbers):  # *numbers is set to arbitrary arguments
    sum = 0  # sum is set to 0
    for number in numbers:
        sum = sum + number  # for every number in numbers, the number is added to the sum, repeats until the last number
    print(sum)  # the sum of all the numbers provided is 55

summationOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
