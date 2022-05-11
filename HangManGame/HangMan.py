import random

words = ["Apple", 'Oranges', "Blub", "Mango", "Coconut"]
chosen_word = random.choice(words).lower()
# print(chosen_word)

chosen_word_fill = []
for chars in chosen_word:
    chosen_word_fill.append("_")
chances = len(chosen_word)
print(f"You have {chances} chances")
isGameOver = False
while chances > 0:
    if chosen_word_fill.count("_") == 0:
        isGameOver = True
        break
    guess = input("Guess a letter: ").lower()
    index = 0
    count = chosen_word.count(guess)
    if count == 0:
        print("Wrong choice")
        print(f"{chances} chances left")
        chances -= 1
        continue
    for chars in chosen_word:
        if chars == guess:
            chosen_word_fill[index] = chars
            count -= 1
            if count == 0:
                chances -= 1
                break
        index += 1

    print(chosen_word_fill)
    print(f"{chances} chances left")

print("Game Over")
if not isGameOver:
    if chosen_word_fill.count("_") > 0:
        print("You lost :(")
    else:
        print("You won :)")