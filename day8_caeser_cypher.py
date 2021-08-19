alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(encode_decode, plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if encode_decode == 'encode':
            new_position = alphabet.index(letter) + shift_amount
        else:
            new_position = alphabet.index(letter) - shift_amount
        if new_position > 25:
             new_position -= 25
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The text is {cipher_text}")

if shift > 25:
    shift = shift%25
caesar(encode_decode=direction, plain_text=text, shift_amount=shift)
