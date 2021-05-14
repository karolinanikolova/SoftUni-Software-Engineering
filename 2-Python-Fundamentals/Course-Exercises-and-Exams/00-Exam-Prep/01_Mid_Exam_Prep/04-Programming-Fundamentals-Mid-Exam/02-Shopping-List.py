# Problem 2. Shopping List
# It’s the end of the week and it is time for you to go shopping, so you need to create a shopping list first.
# Input
# You will receive an initial list with groceries separated by "!".
# After that you will be receiving 4 types of commands, until you receive "Go Shopping!"
# •	Urgent {item} - add the item at the start of the list.
# If the item already exists, skip this command.
# •	Unnecessary {item} - remove the item with the given name, only if it exists in the list.
# Otherwise skip this command.
# •	Correct {oldItem} {newItem} – if the item with the given old name exists, change its name with the new one.
# If it doesn't exist, skip this command.
# •	Rearrange {item} - if the grocery exists in the list, r
# move it from its current position and add it at the end of the list.

shopping_list = input().split("!")

command_data = input()

while command_data != "Go Shopping!":
    command_data = command_data.split()
    command = command_data[0]

    if command == "Urgent":
        item = command_data[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)

    elif command == "Unnecessary":
        item = command_data[1]
        if item in shopping_list:
            shopping_list.remove(item)

    elif command == "Correct":
        old_item = command_data[1]
        new_item = command_data[2]
        if old_item in shopping_list:
            index = shopping_list.index(old_item)
            shopping_list[index] = new_item

    elif command == "Rearrange":
        item = command_data[1]
        if item in shopping_list:
            index = shopping_list.index(item)
            shopping_list.pop(index)
            shopping_list.append(item)

    command_data = input()

print(*shopping_list, sep=", ")
