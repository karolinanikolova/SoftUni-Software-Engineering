numbers_dictionary = {}

while True:
    number_as_string = input()
    if number_as_string == "Search":
        break
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(f"The variable number must be an integer")

line = input()

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
        line = input()
    except KeyError:
        print("Number does not exist in dictionary")

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
        line = input()
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)
