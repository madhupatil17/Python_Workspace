import random

chances = 0
range_of_number = 0

def game_setup():
    global chances, range_of_number
    if input("Choose game level from easy and hard: ") == "hard":
        range_of_number = 100
        chances = 5
    else:
        range_of_number = 50
        chances = 10

def start_game():
    global chances, range_of_number

    random_number = random.randint(0, range_of_number+1)
    print(random_number)
    print(f"I am thinking of a number from 0 to {range_of_number}. ")
    win = False

    while chances > 0:
        print(f"You have {chances} chances remaining\n")
        guess = int(input("Guess a number: "))
        if guess == random_number:
            print("Good work! You won the game.")
            win = True
            break
        else:
            if guess > random_number:
                print("Too high. Guess again")
            else:
                print("Too low. Guess again")
            chances -= 1

    if not win:
        print("You lost. Better luck next time:)")

new_game = True
while new_game:
    game_setup()
    start_game()
    if input("\nDo you want to play a new game? ").lower() == 'y':
        continue
    else:
        break
