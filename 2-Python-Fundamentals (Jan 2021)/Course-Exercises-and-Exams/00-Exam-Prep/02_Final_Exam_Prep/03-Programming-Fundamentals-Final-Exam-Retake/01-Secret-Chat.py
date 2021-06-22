# Programming Fundamentals Final Exam Retake 10.04.2020
# Problem 1. Secret Chat
# You have plenty of free time, so you decide to write a program that conceals and reveals your received messages.
# Go ahead and type it in!
# On the first line of the input you will receive the concealed message. After that, until the "Reveal" command is given,
# you will be receiving strings with instructions for different operations that need to be performed upon the concealed
# message in order to interpret it and reveal its true content. There are several types of instructions, split by ":|:"
# •	InsertSpace:|:{index}
# o	Inserts a single empty space at the given index. The given index will always be valid.
# •	Reverse:|:{substring}
# o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
# o	If not, print "error".
# o	This operation should replace only the first occurrence of the given substring if there are more than one such occurrences.
# •	ChangeAll:|:{substring}:|:{replacement}
# o	Changes all occurrences of the given substring with the replacement text.

message = input()

command = input()

while not command == "Reveal":
    command = command.split(":|:")
    instruction = command[0]

    if instruction == "InsertSpace":
        index = int(command[1])
        message = message[0:index] + " " + message[index:]
        print(message)

    elif instruction == "Reverse":
        substring = command[1]
        reversed_substring = substring[::-1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += reversed_substring
            print(message)
        else:
            print("error")

    elif instruction == "ChangeAll":
        substring = command[1]
        substring_replacement = command[2]
        if substring in message:
            message = message.replace(substring, substring_replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")
