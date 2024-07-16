count_of_lines = int(input())

for i in range(count_of_lines):
    sentence = input().split(' ')
    name = ''
    age = ''
    for word in sentence:
        if '@' in word and '|' in word:
            starting_index = word.index('@') + 1
            ending_index = word.rfind('|')
            name = word[starting_index: ending_index]
        if '#' in word and '*' in word:
            start_age = word.find('#') + 1
            end_age = word.rfind('*')
            age = word[start_age: end_age]
    print(f'{name} is {age} years old.')

