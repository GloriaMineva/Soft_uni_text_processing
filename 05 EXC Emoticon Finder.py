user_input = input()
for i in range(len(user_input)):
    if user_input[i] == ':':
        print(user_input[i : (i + 2)])


