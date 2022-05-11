word = input("Type a word: ")
maximum_repetitions = 0
repeated_letter = ""
index = 0
set_word = set(word)
list_word = list(word)
for letter in set_word:
    letter_count = list_word.count(letter)
    if letter_count > maximum_repetitions:
        maximum_repetitions = letter_count
        repeated_letter = letter
        index = word.index(letter)
print(repeated_letter, "=", maximum_repetitions)
print("Index=", index)
