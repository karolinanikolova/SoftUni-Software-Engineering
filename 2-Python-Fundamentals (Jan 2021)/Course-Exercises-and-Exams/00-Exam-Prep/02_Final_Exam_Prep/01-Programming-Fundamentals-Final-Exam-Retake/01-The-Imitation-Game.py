# Programming Fundamentals Final Exam Retake 15.08.2020
# Problem 1. The Imitation Game
# You are a mathematician during world war 2, who has joined the cryptography team to decipher the enemy's enigma code.
# Your job is to create a program to crack the codes.
# On the first line of the input you will receive the encrypted message. After that, until the "Decode" command is given,
# you will be receiving strings with instructions for different operations that need to be performed upon the concealed
# message to interpret it and reveal its true content. There are several types of instructions, split by '|'
# •	Move {number of letters}
# o	Moves the first n letters to the back of the string.
# •	Insert {index} {value}
# o	Inserts the given value before the given index in the string.
# •	ChangeAll {substring} {replacement}
# o	Changes all occurrences of the given substring with the replacement text.

message = input()

command = input()

while not command == "Decode":
    command = command.split("|")
    action = command[0]

    if action == "Move":
        n_letters = int(command[1])
        index = n_letters
        message = message[index:] + message[:index]

    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]

    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")