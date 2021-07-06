# 1.	Reverse Numbers with a Stack
# Write a program that reads from the console a string with N integers, separated by a single space,
# and reverses them using a stack. Print the reversed integers on one line, separated by a single space.

integers = input().split()

stack = []

while integers:
    stack.append(integers.pop())

print(" ".join(stack))
