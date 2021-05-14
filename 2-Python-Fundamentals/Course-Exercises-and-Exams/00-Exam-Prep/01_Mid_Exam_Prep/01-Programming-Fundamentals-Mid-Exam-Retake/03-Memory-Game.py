# 03. Memory game
# Write a program, which receives a sequence of elements. Each element in the sequence will have a twin.
# Until the player receives "end" from the console, he will receive strings with two integers separated by space,
# which represent the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence you
# should add two matching elements in the following format "-{number of moves until now}a" at the middle of the sequence
# and print this message on the console:
# "Invalid input! Adding additional elements to the board"

sequence = input().split()

command_data = input()

moves = 0

while not command_data == "end":
    index1, index2 = [int(el) for el in command_data.split()]
    moves += 1

    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(sequence) or index2 >= len(sequence):
        added_element = '-' + str(moves) + 'a'
        middle_index = int(len(sequence) / 2)
        sequence.insert(middle_index, added_element)
        sequence.insert(middle_index, added_element)
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence[index1] == sequence[index2]:
            matching_element = sequence[index1]
            indexes = [index1, index2]
            for index in sorted(indexes, reverse=True):
                del sequence[index]
            print(f"Congrats! You have found matching elements - {matching_element}!")
        else:
            print("Try again!")

    if not sequence:
        print(f"You have won in {moves} turns!")
        break

    command_data = input()

if sequence:
    print("Sorry you lose :(")
    print(' '.join(sequence))

