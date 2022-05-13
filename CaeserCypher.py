message = input("enter a text to encrypt: ")
encrypt_message = ''
try:
    shift = int(input("shift value: "))
except ValueError:
    print("shift value must be number")
    exit()

for character in message:
    if character.isalpha():
        if character.isupper():
            if ord(character) + shift > ord('Z'):
                encrypt_message += chr(ord(character) + shift - 26)
            else:
                encrypt_message += chr(ord(character) + shift)
        else:
            if ord(character) + shift > ord('z'):
                encrypt_message += chr(ord(character) + shift - 26)
            else:
                encrypt_message += chr(ord(character) + shift)
    else:
        encrypt_message += character

print(encrypt_message)
