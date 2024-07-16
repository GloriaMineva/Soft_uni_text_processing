to_remove = input()
to_filter = input()
while to_remove in to_filter:
    to_filter = to_filter.replace(to_remove, '')
print(to_filter)