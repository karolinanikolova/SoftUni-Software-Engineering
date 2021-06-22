chat = []

command = input()

while not command == "end":
    command = command.split()
    action = command[0]

    if action == "Chat":
        message = command[1]
        chat.append(message)
    elif action == "Delete":
        message = command[1]
        if message in chat:
            chat.remove(message)
    elif action == "Edit":
        message_to_edit = command[1]
        message_edited = command[2]
        if message_to_edit in chat:
            index_of_message_to_edit = chat.index(message_to_edit)
            chat[index_of_message_to_edit] = message_edited
        # for index, value in enumerate(chat):
        #     if value == message_to_edit:
        #         chat[index] = message_edited
    elif action == "Pin":
        message = command[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif action == "Spam":
        messages = command[1:]
        for message in messages:
            chat.append(message)

    command = input()

print(*chat, sep = "\n")
