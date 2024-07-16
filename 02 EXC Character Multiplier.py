first, second = input().split()
multiplication_sum = 0
if len(first) == len(second):
    for i in range(len(first)):
        multiplication_sum += ord(first[i]) * ord(second[i])
elif len(first) > len(second):
    for i in range(len(second)):
        multiplication_sum += ord(first[i]) * ord(second[i])
    difference = len(first) - len(second)
    for letter in first[-difference:]:
        multiplication_sum += ord(letter)
else:
    for i in range(len(first)):
        multiplication_sum += ord(first[i]) * ord(second[i])
    difference = len(second) - len(first)
    for letter in second[-difference:]:
        multiplication_sum += ord(letter)

print(multiplication_sum)