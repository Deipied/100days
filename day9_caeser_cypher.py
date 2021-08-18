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

caesar(encode_decode=direction, plain_text=text, shift_amount=shift)

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         new_position = alphabet.index(letter) + shift_amount
#         if new_position > 25:
#             new_position -= 25
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(encoded_text, shifted_amount):
#     cipher_text = ""
#     for letter in encoded_text:
#         new_position = alphabet.index(letter) - shifted_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The decoded text is {cipher_text}")

# if direction == 'encode':
#     encrypt(plain_text = text, shift_amount = shift)
# else:
#     decrypt(encoded_text = text, shifted_amount = shift)