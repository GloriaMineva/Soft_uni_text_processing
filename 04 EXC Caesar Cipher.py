message = input()
encrypted_message = ''
for letter in message:
    encrypted_letter = chr(ord(letter) + 3)
    encrypted_message += encrypted_letter
print(encrypted_message)