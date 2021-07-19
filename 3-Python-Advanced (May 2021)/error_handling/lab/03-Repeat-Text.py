# 3.	Repeat Text
# Write a program that receives text on the first line and times (to repeat the text) that must be an
# integer. If the user passes non-integer type for the times variable,
# handle the exception and print a message
# "Variable times must be an integer".

text = input()

try:
    number = int(input())
except ValueError:
    print("Variable times must be an integer")
else:
    # With else - Only if you manage to do the try (no exception), then it will do it
    print(text * number)
finally:
    "Print no matter what"