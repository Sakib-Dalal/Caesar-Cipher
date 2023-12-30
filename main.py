alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    new_text = ""
    for letter in plain_text:
        if letter == " ":
            new_text += " "
        else:
            position = alphabet.index(letter) + shift_amount
            new_text += alphabet[position]
    print(f"The encrypted text is: {new_text}")


def decrypt(encrypt_text, shift_amount):
    new_text = ""
    for letter in encrypt_text:
        if letter == " ":
            new_text += " "
        else:
            position = alphabet.index(letter) - shift_amount
            new_text += alphabet[position]
    print(f"The decoded text is: {new_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(encrypt_text=text, shift_amount=shift)
else:
    print("Invalid Input!")