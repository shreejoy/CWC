import random

USER_INPUT = ""
USER_POINTS = 0

COMPUTER_INPUT = ""
COMPUTER_POINTS = 0

STOP_GAME = False
MAX_ROUNDS = 3
COMPLETED_ROUNDS = 0
ACCEPTED_INPUTS = ['R', 'P', 'S']

while not STOP_GAME and COMPLETED_ROUNDS < MAX_ROUNDS:
    print("\nStarting Round!")
    # Ask user's initial input
    USER_INPUT = input("User's choice: ")
    # Make a random choice for computer input
    COMPUTER_INPUT = random.choice(ACCEPTED_INPUTS)
    # Validate input or ask them to enter correct again.
    while USER_INPUT not in ACCEPTED_INPUTS:
        print("Invalid Input. Please enter one of accepted inputs >",
              str(ACCEPTED_INPUTS))
        USER_INPUT = input("User's choice: ")
    else:
        print(
            f"Input success! \n\nUser's input is \n{USER_INPUT}\n\nComputer's input is \n{COMPUTER_INPUT}\n")

        if USER_INPUT == 'R' and COMPUTER_INPUT == 'P':
            COMPUTER_POINTS += 1
            print("Computer won this round.")
        elif USER_INPUT == 'P' and COMPUTER_INPUT == 'S':
            COMPUTER_POINTS += 1
            print("Computer won this round.")
        elif USER_INPUT == 'S' and COMPUTER_INPUT == 'R':
            COMPUTER_POINTS += 1
            print("Computer won this round.")
        elif USER_INPUT == 'R' and COMPUTER_INPUT == 'S':
            USER_POINTS += 1
            print("User won this round.")
        elif USER_INPUT == 'P' and COMPUTER_INPUT == 'R':
            USER_POINTS += 1
            print("User won this round.")
        elif USER_INPUT == 'S' and COMPUTER_INPUT == 'P':
            USER_POINTS += 1
            print("User won this round.")
        else:
            USER_POINTS += 1
            COMPUTER_POINTS += 1
            print("Tie round!")

        COMPLETED_ROUNDS += 1
        if COMPLETED_ROUNDS < 3:
            STOP_GAME = False if input("Would you play another game? Enter 'y' or 'n': ") == 'y' else True

print(f"\n{COMPLETED_ROUNDS} round(s) completed. Computer points are {COMPUTER_POINTS} and user points are {USER_POINTS}")
if COMPUTER_POINTS == USER_POINTS:
    print("Game tied!")
elif COMPUTER_POINTS > USER_POINTS:
    print("Computer won the game!")
else:
    print("User won this game.!")
