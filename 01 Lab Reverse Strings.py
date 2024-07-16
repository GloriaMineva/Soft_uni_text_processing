reverse_word = ''
while True:
    word = input()
    if word == 'end':
        break
    # reverse_word = word[::-1]
    reverse_word = ''.join(reversed(word))
    print(f'{word} = {reverse_word}')