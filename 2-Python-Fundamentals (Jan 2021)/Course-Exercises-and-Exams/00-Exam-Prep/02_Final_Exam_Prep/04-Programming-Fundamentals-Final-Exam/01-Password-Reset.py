# Problem 1. Password Reset
# Yet again you have forgotten your password... Naturally it`s not the first time this has happened.
# Actually you got so tired of it that you decided to help yourself with a smart solution.
#
# Write a password reset program that performs a series of commands upon a predefined string.
# First, you will receive a string and afterwards, until the command "Done" is given, you will be receiving strings
# with commands split by a single space. The commands will be the following:
# •	TakeOdd
# o	 Takes only the characters at odd indices and concatenates them together to
# obtain the new raw password and then prints it.
# •	Cut {index} {length}
# o	Gets the substring with the given length starting from the given index from the password and removes its first
# occurrence of it, then prints the password on the console.
# o	The given index and length will always be valid.
# •	Substitute {substring} {substitute}
# o	If the raw password contains the given substring, replaces all of its
# occurrences with the substitute text given and prints the result.
# o	If it doesn’t, prints "Nothing to replace!"

password = input()

command = input()

while not command == "Done":
    command = command.split()
    action = command[0]

    if action == "TakeOdd":
        new_password = ""
        password = "".join([new_password + password[index] for index in range(len(password)) if index % 2 == 1])
        print(password)

    elif action == "Cut":
        start_index = int(command[1])
        length = int(command[2])
        substring_to_be_cut = password[start_index:start_index+length]
        password = password.replace(substring_to_be_cut, "", 1)
        print(password)

    elif action == "Substitute":
        substring_to_be_substituted = command[1]
        substitute = command[2]

        if substring_to_be_substituted in password:
            password = password.replace(substring_to_be_substituted, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")
