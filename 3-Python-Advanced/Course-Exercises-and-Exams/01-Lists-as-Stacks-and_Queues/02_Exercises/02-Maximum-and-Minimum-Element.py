# 2. Maximum and Minimum Element
# You have an empty sequence. You will receive an integer – N. On the next N lines you will receive queries.
# Each query is one of these four types:
# '1 x' – Push the element x into the stack.
# '2' – Delete the element at the top of the stack.
# '3' – Print the maximum element in the stack.
# '4' – Print the minimum element in the stack.
# After you go through all the queries, print the stack from the top to the bottom in the following format:
# "{n}, {n1}, {n2} …, {nn}"
# Constraints
# •	It is guaranteed that each query is valid
# •	1 ≤ N ≤ 105
# •	1 ≤ x ≤ 109
# •	1 ≤ type ≤ 4

N = int(input())

stack = []
stack_max = []
stack_min = []

for _ in range(N):
    command = input()

    if command.startswith("1"):
        stack.append(command.split()[-1])
        if not stack_max:
            stack_max.append(int(command.split()[-1]))
        else:
            if int(command.split()[-1]) > stack_max[-1]:
                stack_max.append(int(command.split()[-1]))

        if not stack_min:
            stack_min.append(int(command.split()[-1]))
        else:
            if int(command.split()[-1]) < stack_min[-1]:
                stack_min.append(int(command.split()[-1]))

    elif command.startswith("2"):
        if stack_max:
            if stack_max[-1] == int(stack[-1]):
                stack_max.pop()
        if stack_min:
            if stack_min[-1] == int(stack[-1]):
                stack_min.pop()
        if stack:
            stack.pop()

    elif command.startswith("3"):
        if stack_max:
            print(stack_max[-1])

    elif command.startswith("4"):
        if stack_min:
            print(stack_min[-1])

reversed_stack = []

while stack:
    reversed_stack.append(stack.pop())

print(', '.join(reversed_stack))