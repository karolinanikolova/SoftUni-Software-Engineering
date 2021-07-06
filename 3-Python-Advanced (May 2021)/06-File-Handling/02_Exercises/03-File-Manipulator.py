# 3.	File Manipulator
# Create a program that will receive commands until the command "End". The commands can be:
# •	"Create-{file_name}" - Creates the given file with an empty content.
# If the file already exists, remove the existing text in it (as if the file is created again)
# •	"Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist,
# create it, and add the content
# •	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences
# of the old string with the new string. If the file does not exist, print: "An error occurred"
# •	"Delete-{file_name}" - Delete the file. If the file does not exist,
# print: "An error occurred"

import os

data = input()

while not data == "End":
    command, *rest_data = data.split('-')

    if command == "Create":
        with open(rest_data[0], 'w'):
            pass

    elif command == "Add":
        filename, line = rest_data
        with open(filename, 'a') as file:
            file.write(line + '\n')

    elif command == "Replace":
        filename, old, new = rest_data

        try:
            with open(filename, 'r') as file:
                content = file.read()

            with open(filename, 'w') as file:
                content = content.replace(old, new)
                file.write(content)
        except Exception:
            print("An error occurred")
            data = input()
            continue

    elif command == "Delete":
        try:
            os.remove(rest_data[0])
        except FileNotFoundError:
            print("An error occurred")

    data = input()