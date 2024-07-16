data = input()
rage_message = ''
temp_phrase = ''
multiplier_num = ''
for i in range(len(data)):
    if not data[i].isnumeric():
        temp_phrase += data[i]
    else:
        for next_num in range(i, len(data)):
            if not data[next_num].isnumeric():
                break
            multiplier_num += data[next_num]
        temp_phrase = temp_phrase.upper() * int(multiplier_num)
        rage_message += temp_phrase
        temp_phrase = ''
        multiplier_num = ''

symbols_counter = len(set(rage_message))
print(f'Unique symbols used: {symbols_counter}')
print(rage_message)

