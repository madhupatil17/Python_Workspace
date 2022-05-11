from Graphics import logo, vs_logo
from GameData import data
import random, pyfiglet
import common_functions as common


def pick_data(list_of_entities):
    entity1 = set()
    entity2 = set()
    entity1 = random.choice(list_of_entities)
    entity2 = random.choice(list_of_entities)

    while entity1.items() == entity2.items():
        entity2 = random.choice(list_of_entities)
    return list([entity1, entity2])

def start_game():
    ##Initializing
    print(logo, end = '\n')
    print("*"*120, end='\n\n')

    score = 0
    while True:
        comparison_data = pick_data(data)
        followers1 = comparison_data[0]['follower_count']
        followers2 = comparison_data[1]['follower_count']
        win = False

        print(f"Compare A:  {comparison_data[0]['name']}, {comparison_data[0]['description']}, {comparison_data[0]['country']}")
        print(vs_logo, end='')
        print(f"Compare B:  {comparison_data[1]['name']}, {comparison_data[1]['description']}, {comparison_data[1]['country']}")

        guess = input("Who has most followers? Type A or B -> ").lower()
        if guess == 'a':
            if followers1 > followers2:
                score += 1
                win = True
                print("Correct!!")
                print(f"Your score is: {score}")
        elif guess == 'b':
            if followers2 > followers1:
                score += 1
                win = True
                print("Correct!!")
                print(f"Your score is: {score}")
        else:
            print("Choose only from A or B")

        if not win:
            print("Wrong choice")
            print(f"Your final score is: {score}")
            print(pyfiglet.figlet_format("Game Over", font="cybermedium"))
            break

        print("*" * 120, end='\n\n')

def play():
    new_game = True
    start_game()
    while True:
        if input("Do you wish to play another game? Type yes or no: ").lower() == 'yes':
            common.cls()
            start_game()
        else:
            print("Thank you for playing the game.")
            break

play()
