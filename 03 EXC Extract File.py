file_path = input()
starting_index = file_path.rfind('\\') + 1
end_index = file_path.index('.')
name = file_path[starting_index: end_index]
extension = file_path[end_index + 1:]
print(f'File name: {name}')
print(f'File extension: {extension}')


