# Math quiz game

import random

print("Welcome to Math Quiz Game")
print("Rules : Get 10 correct answers before losing all 3 of your lives ")
print("")

lives = 3  # number of lives
score = 0  # score starts at 0
n = 1   # this the number of question

# everything inside this loop loops until you win or you lose all your lives
while lives > 0:  # loop repeats if your life is >= 1
    r1 = int(random.randint(0, 1000))  # first random number variable
    r2 = int(random.randint(0, 1000))  # second random number variable
    operation = random.choice(['+' ,'-' ,'*', '%'])  # randomly selects an operation inside the list

    if operation == '*':  # condition to get multiplication questions
        if r1 < 400 and r2 < 400:  # condition to limit multiplication numbers under 400 to keep the number low
            correctAnswer = r1 * r2
            print(r1, r2, correctAnswer)  # <--comment this line as it is a cheat sheet for testing
            print("Question", n, ":", r1, "*", r2, "?")
        else:
            continue  # CONTINUE is used to skip the current iteration and proceed to the next

    elif operation == '%':  # condition to get modulo questions
        if r1 < 400 and r2 < 400:  # condition to limit modulo numbers under 400 to keep the number low
            correctAnswer = r1 % r2
            print(r1, r2, correctAnswer)  # <--comment this line as it is a cheat sheet for testing
            print("Question", n, ":", r1, "%", r2, "?")
        else:
            continue  # CONTINUE is used to skip the current iteration and proceed to the next

    elif operation == '-':  # condition to get subtraction questions
        correctAnswer = r1 - r2
        print(r1, r2, correctAnswer)  # <--comment this line as it is a cheat sheet for testing
        print("Question", n, ":", r1, "-", r2, "?")

    else :  # this "ELSE" condition is set to give addition problems
        correctAnswer = r1 + r2
        print(r1, r2, correctAnswer)  # <--comment this line as it is a cheat sheet for testing
        print("Question", n, ":", r1, "+", r2, "?")

    answer = int(input("Enter your answer : "))  # gets the input to get answer
    print(" ")

    if answer == correctAnswer:  # condition for correct answers
        score = score + 1  # this updates the score if your answer is correct
        print("Answer : ", answer)
        print("Your answer is Correct!")
        print("Score : ", score)
        print("Lives remaining : ", lives)
        print(" ")

        if score == 5:  # if you get 5 correct answers before losing all lives, you win and the loop stops
            print("You won!")
            print("Score : ", score)
            print("Lives remaining : ", lives)
            break

    else:  # this "ELSE" condition is when you get wrong answers and subtracts 1 life
        lives = lives - 1  # this updates the lives if you get an answer wrong
        print("Wrong Answer!")
        print("Correct Answer : ", correctAnswer)
        print("Score : ", score)
        print("Lives remaining: ", lives)
        print(" ")

    n = n + 1  # this updates what number is the next question

else:  # this "ELSE" condition is set for when you lost all 3 of your lives and then the loop stops
    print("You lost")
    print("Score : ", score)
