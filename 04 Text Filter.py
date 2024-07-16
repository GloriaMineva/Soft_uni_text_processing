banned_words = input().split(', ')
text = input()
for word in banned_words:
    replace_with = '*' * len(word)
    while word in text:
        text = text.replace(word, replace_with)
print(text)