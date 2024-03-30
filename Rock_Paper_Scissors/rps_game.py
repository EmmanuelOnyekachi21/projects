"""This is the game file"""

import random
import os
import re


def check_play_status():
    """
    Asks the user if he/she intends to play again

    Raises: ValueError if user inputs any response aside yes or no.
    """
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input("Do you wish to play again? (Yes or No): ")
            if response.lower() not in valid_responses:
                raise ValueError("Yes or No only")
            if response.lower() == "yes":
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Thanks for playing!")
                exit()
        except ValueError as err:
            print(err)

def play_rps():
    """
    Plays a classic game of Rock-Paper_Scissors against the computer.

    This function allow users to play multiple rounds of Rock-Paper-Scissors until they choose to exit.  In each round, the user selects their choice of Rock (R), Paper (P), or Scissors (S), and the computer randomly selects
its choice. The winner is determined based on the standard Rock-Paper-Scissors
rules.
    
    Functions:
        check_play_status: Prompts the user to play again and returns True if they choose 'yes' or exits the program otherwise.

    Returns:
        None.
    """
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("Rock, Paper, Scissors - Shoot!")

        user_choice = input("Choose your weapon"
                            "[R]ock, [P]aper, or [S]cissors: ")
        if not re.match("[SsRrPp]", user_choice):
            print("Please choose a letter:")
            print("[R]ock, [P]aper, or [S]cissors: ")
            continue

        print(f"You chose: {user_choice}")

        choices = ["R", "P", "S"]
        opp_choice =random.choice(choices)

        print(f"I choose: {opp_choice}")

        if opp_choice == user_choice.upper():
            print("Tie!")
            play = check_play_status()
        elif opp_choice == "R" and user_choice.upper() == "S":
            print("Rock beats scissors, I win!")
            play = check_play_status()
        elif opp_choice == "S" and user_choice.upper() == "P":
            print("Scissors beats Paper, I win!")
            play = check_play_status()
        elif opp_choice == "P" and user_choice.upper() == "R":
            print("Paper beats Rock, I win!")
            play = check_play_status()
        else:
            print("You win!\n")
            play = check_play_status()

if __name__ == "__main__":
    play_rps()

