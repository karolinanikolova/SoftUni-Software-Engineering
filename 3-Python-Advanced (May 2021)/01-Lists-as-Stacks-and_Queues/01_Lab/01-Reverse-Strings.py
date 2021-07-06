# 1.	Reverse Strings
# Write program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console

word = list(input())

stack = []

while len(word) > 0:
    stack.append(word.pop())

print(''.join(stack))

