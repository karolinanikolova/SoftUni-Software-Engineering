# 3.	 Extract File
# Write a program that reads the path to a file and subtracts the file name and its extension.

path = input()

for index in range(len(path)-1, 0, -1):
    if path[index] == ".":
        start_index_extension = index + 1
        end_index_filename = index - 1
    elif path[index] == "\\":
        start_index_filename = index + 1
        break

filename = path[start_index_filename:end_index_filename+1]
extension = path[start_index_extension:]

print(f"File name: {filename}")
print(f"File extension: {extension}")
