from morse3 import Morse as m

encrypted = input().split(' | ')
print(encrypted)
deciphered = ''
for word in encrypted:
    deciphered += m(word).morseToString().upper()
    deciphered += ' '

print(deciphered)