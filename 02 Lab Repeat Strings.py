data_input = input().split()
concatenated_string = ''
for word in data_input:
    multiplied_word = word * len(word)
    concatenated_string += multiplied_word
print(concatenated_string)