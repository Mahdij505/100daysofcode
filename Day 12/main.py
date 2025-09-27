import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def set_difficulty():
    game_hardness = input("Choose a difficulty. Type 'easy' or 'hard':    ").lower()
    if game_hardness == "hard":
        return HARD_ATTEMPTS
    return EASY_ATTEMPTS

def check_guess(guess, answer):
    if answer > guess:
        print("Too High!")
    elif answer < guess:
        print("Too Low!")
    else:
        print(f"You got it! The answer was {guess}.")
        return True

    return False

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    guessed_num = random.randint(1, 100)

    attempts = set_difficulty()

    while attempts > 0 :
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guessed_num = int(input("Make a guess:    "))

        if check_guess(user_guessed_num, guessed_num):
            break

        attempts -= 1

        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")

    if input("Play game again? 'y' or 'n' ").lower() == "y":
        print("\n" * 20)
        game()

game()