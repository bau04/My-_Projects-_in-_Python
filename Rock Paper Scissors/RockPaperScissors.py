import random

# define the options for the game using a tuple
options = ("rock", "paper", "scissors")

# Initialize a flag to control the game loop
playing = True

# Main game loop
while playing:

    # Initialize player's choice and randomly select computer's choice
    player = None
    computer = random.choice(options)  # makes computer variable choose randomly between the provided options

    # Prompt the player to enter their choice and validate it
    while player not in options:  # loops back to choices if the user input is not in the choices
        player = input("Enter your choice (rock, paper, scissors): ")

    # Display player and computer choices
    print(f"Player : {player}")
    print(f"Computer : {computer}")

    # Determine the game outcome
    if player == computer:
        print("It's a tie!")

    elif player == "rock" and computer == "scissors":
        print("You Win!")

    elif player == "paper" and computer == "rock":
        print("You Win!")

    elif player == "scissors" and computer == "paper":
        print("You Win!")

    else:
        print("You lose!")

    print()

    # Ask if the player wants to play again
    if not input("Do you want to play again (y or n)? ").lower() == "y":
        playing = False
        print()

# Print a “Thank You” message when the game ends
print("Thanks for Playing")
