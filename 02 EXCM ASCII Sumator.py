starting_point = ord(input())
end_point = ord(input())
phrase = input()
sum = 0
for letter in phrase:
    if starting_point < ord(letter) < end_point:
        sum += ord(letter)
print(sum)