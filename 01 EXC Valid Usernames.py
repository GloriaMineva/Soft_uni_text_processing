usernames_lst = input().split(', ')
validated = []

for username in usernames_lst:
    if 3 <= len(username) <= 16:
        only_valid = True
        for letter in username:
            if not (ord(letter) == 45 or
               ord(letter) == 95 or
               48 <= ord(letter) <= 57 or
               97 <= ord(letter.lower()) <= 122):
                only_valid = False
        if only_valid == True:
            validated.append(username)
for word in validated:
    print(word)


