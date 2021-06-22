# Programming Fundamentals Final Exam 04.04.2020
# Problem 1. Activation Keys
# You are about to make some good money, but first you need to think of a way to verify who paid for your product and who didn`t.
# You have decided to let people use the software for a free trial period and then require an activation key in order
# to continue to use the product. The last step before you could cash out is to design a program that creates unique
# activation keys for each user. So, waste no more time and start typing!
#
# The first line of the input will be your raw activation key. It will consist of letters and numbers only.
# After that, until the "Generate" command is given, you will be receiving strings with instructions for different
# operations that need to be performed upon the raw activation key.
# There are several types of instructions, split by ">>>":
# •	Contains>>>{substring} – checks if the raw activation key contains the given substring.
# o	If it does prints: "{raw activation key} contains {substring}".
# o	If not, prints: "Substring not found!"
# •	Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}
# o	Changes the substring between the given indices (the end index is exclusive) to upper or lower case.
# o	All given indexes will be valid.
# o	Prints the activation key.
# •	Slice>>>{startIndex}>>>{endIndex}
# o	Deletes the characters between the start and end indices (end index is exclusive).
# o	Both indices will be valid.
# o	Prints the activation key.

activation_key = input()

command = input()


def contain_check(act_key, substr):
    if substr in act_key:
        return f"{act_key} contains {substr}"
    return "Substring not found!"


def flip_and_replace(act_key, case, start_i, end_i):
    if case == "Upper":
        act_key = act_key[:start_i] + act_key[start_i:end_i].upper() + act_key[end_i:]
    elif case == "Lower":
        act_key = act_key[:start_i] + act_key[start_i:end_i].lower() + act_key[end_i:]
    return act_key


def slice_and_delete(act_key, start_i, end_i):
    act_key = act_key.replace(act_key[start_i:end_i], "")
    return act_key

while not command == "Generate":
    command = command.split(">>>")
    instruction = command[0]

    if instruction == "Contains":
        substring = command[1]
        print(contain_check(activation_key, substring))

    elif instruction == "Flip":
        case = command[1]
        start_index = int(command[2])
        end_index = int(command[3])

        activation_key = flip_and_replace(activation_key, case, start_index, end_index)
        print(activation_key)

    elif instruction == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])

        activation_key = slice_and_delete(activation_key, start_index, end_index)
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")