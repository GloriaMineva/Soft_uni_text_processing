sum = 0
game_data = input().split()
for phrase in game_data:
    first, number, last = phrase[0], int(phrase[1: -1]), phrase[-1]
    if first.islower():
        number *= (ord(first) - 96)
    elif first.isupper():
        number /= (ord(first.lower()) - 96)
    if last.isupper():
        number -= (ord(last.lower()) - 96)
    elif last.islower():
        number += (ord(last) - 96)
    sum += number
print(f'{sum:.2f}')