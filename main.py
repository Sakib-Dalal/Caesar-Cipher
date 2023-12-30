# Author of the code "Sakib Dalal"
from art import logo
import string

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        new_text = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter) + shift
                new_text += alphabet[position]
            else:
                new_text += letter
        print(f"The encrypted text is: {new_text}")

    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        new_text = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter) - shift
                new_text += alphabet[position]
            else:
                new_text += letter
        print(f"The decoded text is: {new_text}")

    else:
        print("Invalid Input!")


print(logo)
is_stop = False
while not is_stop:
    caesar()
    usr_input = input("Type 'Yes' want to go again, Otherwise type 'No': ").lower()
    if usr_input == 'yes':
        is_stop = False
        print()
    else:
        is_stop = True
        print("Good By.")
