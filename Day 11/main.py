import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players = {
    "user" : [],
    "computer" : []
}

continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

def random_card():
    return random.choice(cards)

def init():
    print(art.logo)
    players["computer"].append(random_card())
    for _ in range(0,2):
        players["user"].append(random_card())

def sum_calculator(list):
    return sum(list)

def check_ace(player):
    for card in player:
        if card == 11 and sum_calculator(players[player]) > 21:
            players[player][players[player].index(card)] = 1

game_is_over = False

def first_check_winner():
        if sum_calculator(players["user"]) == sum_calculator(players["computer"]):
            print_final()
            print("Draw 🙃")
        if sum_calculator(players["user"]) == 21:
            print_final()
            print("Win with a Blackjack 😎")
        if  sum_calculator(players["user"]) > 21:
            print_final()
            print("You went over. You lose 😭")
        else:
            return False

        return True

def final_check_winner():
    if sum_calculator(players["user"]) == sum_calculator(players["computer"]):
        print_final()
        print("Draw 🙃")
    if sum_calculator(players["computer"]) < sum_calculator(players["user"]):
        print_final()
        print("Win with a Blackjack 😎")
    elif sum_calculator(players["computer"]) > 21:
        print_final()
        print("Opponent went over. You win 😁")
    elif sum_calculator(players["computer"]) > sum_calculator(players["user"]):
        print_final()
        print("You lose 😤")

def print_final():
    print(f"Your final hand: {players["user"]}, final score:{sum_calculator(players["user"])}")
    print(f"Computer's final hand: {players["computer"]}, final score:{sum_calculator(players["computer"])}")

def reset_players():
    players["user"] = []
    players["computer"] = []

def black_jack():
    global continue_game

    print(f"Your cards: {players["user"]}, current score: {sum_calculator(players["user"])}")
    print(f"Computer's first card:{players["computer"][0]}")
    if first_check_winner():
        continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

        if continue_game == "y":
            reset_players()
            print("\n" * 100)
        return

    get_another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()


    if get_another_card == "n" :
        while sum_calculator(players["computer"]) < 17:
            players["computer"].append(random_card())
            check_ace("computer")
        print_final()
        final_check_winner()
        reset_players()
        continue_game =  input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
        return


    if get_another_card == "y":
        players["user"].append(random_card())
        check_ace("user")
        black_jack()

while continue_game == "y":
    init()
    black_jack()


