import art
from game_data import data
import random


def choose_random_index(i_a):
    random_index = random.randint(0, len(data)-1)
    if random_index == i_a:
        return choose_random_index(i_a)
    else:
        return random_index

def check_correct_answer(i_a, i_b):
    if data[i_a]['follower_count'] > data[i_b]['follower_count']:
        return i_a
    elif data[i_a]['follower_count'] < data[i_b]['follower_count']:
        return i_b

def game():
    score = 0
    game_is_running = True
    index_a = random.randint(0, len(data)-1)
    while game_is_running:
        print(art.logo)
        if score != 0 :
            print(f"You're right! Current score: {score}")
        index_b = choose_random_index(index_a)
        correct_answer = check_correct_answer(index_a, index_b)
        print(f"Compare A: {data[index_a]['name']}, {data[index_a]['description']}, from {data[index_a]['country']}")
        print(art.vs)
        print(f"Against B: {data[index_b]['name']}, {data[index_b]['description']}, from {data[index_b]['country']}")
        user_guess = input("Who has more followers? Type 'A' or 'B':    ").upper()

        if user_guess == "A" and correct_answer == index_a:
            score += 1
        elif user_guess == "B" and correct_answer == index_b:
            score += 1
            index_a = index_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    if input("Do you want to play the game again? 'y' or 'n':   ").lower() == "y":
        game()

game()