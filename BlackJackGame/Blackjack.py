import random
import pyfiglet
import common_functions

list_of_cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]*4
computers_cards = []
player_cards = []

def give_a_card_to_computers():
    computers_cards.append(random.choice(list_of_cards))
    print("A card is served to Computer")

def give_a_card_to_player():
    player_cards.append(random.choice(list_of_cards))
    print("A card is served to Player")

def return_card_holdings(role, holdings):
    sum_of_holdings = 0
    if role == "player":
        if "ace" in holdings:
            count_of_aces = holdings.count("ace")
            value_of_ace = int(input(f"There is/are {count_of_aces} ace in your holdings. What value do you want to assign to ace? "))
            for aces in range(0, count_of_aces):
                sum_of_holdings += value_of_ace

    for card in holdings:
        if card not in ["ace", "jack", "queen", "king"]:
            sum_of_holdings += card
        elif card in ["jack", "queen", "king"]:
            sum_of_holdings += 10
    if role == "computers":
        for counts_of_ace in range(0, holdings.count("ace")):
            if sum_of_holdings == 20 and "ace" in holdings:
                sum_of_holdings += 1
            elif sum_of_holdings < 20 and "ace" in holdings:
                sum_of_holdings += 11
    return sum_of_holdings


def initial_serve():
    give_a_card_to_player()
    give_a_card_to_computers()
    give_a_card_to_player()
    give_a_card_to_computers()
    print()
    number_of_cards = 2
    print(f"Player has {number_of_cards} card", player_cards)
    print(f"Computer has {number_of_cards} cards, one of them is:", random.choice(computers_cards))
    print()


def start_game():
    end_of_game = False
    print(pyfiglet.figlet_format("BlackJack"))
    initial_serve()
    print("Sum of your holding is:", return_card_holdings("player", player_cards))

    while not end_of_game:
        if input("Do you wish for one more card? ").lower() == 'y':
            print()
            give_a_card_to_player()
            print("You have:", player_cards)
            print("Sum of your holding is:", return_card_holdings("player", player_cards))
            if return_card_holdings("player", player_cards) < 21:
                print()
                if return_card_holdings("computer", computers_cards) < 17:
                    give_a_card_to_computers()
                    if return_card_holdings("computers", computers_cards) > 21:
                        print(pyfiglet.figlet_format("Bust. Computer lost!", font="cybermedium"))
                        end_of_game = True
            else:
                print(pyfiglet.figlet_format("Bust. You lost!", font="cybermedium"))
                end_of_game = True
        else:
            if return_card_holdings("computers", computers_cards) == return_card_holdings("player", player_cards):
                print(pyfiglet.figlet_format("It is a Draw match", font="cybermedium"))
            elif return_card_holdings("computers", computers_cards) > return_card_holdings("player", player_cards):
                print(pyfiglet.figlet_format("Computer won the match", font="cybermedium"))
            else:
                print(pyfiglet.figlet_format("You won the match", font="cybermedium"))
            end_of_game = True

common_functions.cls()
if input("Do you want to play BlackJack? Press 'y' for Yes and 'n' for No-->  ").lower() == 'y':
    start_game()
    print("Computer has:", computers_cards)
    print("You have:", player_cards)

    new_game = True
    while new_game:
        if input("Do you wish to play a new game? ").lower() == 'y':
            common_functions.cls()
            player_cards.clear()
            computers_cards.clear()
            start_game()
            print("Computer has:", computers_cards)
            print("You have:", player_cards)
        else:
            new_game = False
            print(pyfiglet.figlet_format("Game Over.\nThank you for playing."))
else:
    print("Good for you!")