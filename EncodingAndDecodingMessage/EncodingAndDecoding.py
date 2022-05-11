import string
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def ceasar_cipher(choose_task, message, shift_number):
    final_message = ""
    if choose_task == "decode":
        shift_number *= -1
    for letter in message:
        if letter in alphabets:
            original_letter_index = alphabets.index(letter)
            shifted_letter = alphabets[original_letter_index + shift_number]
            final_message += shifted_letter
        else:
            final_message += letter
    print("Final message:", final_message)

while True:
    choose_task = input("Encode or Decode: ").lower()

    if not choose_task in ["encode", "decode"]:
        print("Not a valid input. Choose from 'Encode' or 'Decode'")
        continue

    message = input("Type your message: ")
    shift_number = int(input("Enter shift number: "))
    shift_number %= 26
    ceasar_cipher(choose_task, message, shift_number)
    wish_to_continue = input("Do you wish to continue? Type 'Yes' or 'No': ").lower()
    if wish_to_continue == "yes":
        continue
    elif wish_to_continue == "no":
        break


