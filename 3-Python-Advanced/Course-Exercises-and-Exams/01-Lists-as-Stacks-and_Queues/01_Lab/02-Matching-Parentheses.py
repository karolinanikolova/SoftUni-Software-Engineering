# 2.	Matching Parentheses
# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.

string = list(input())

stack_index = []

for index in range(len(string)):

    if string[index] == "(":
        stack_index.append(index)
    elif string[index] == ")":
        start_index = stack_index.pop()
        end_index = index
        parentheses_set = string[start_index:end_index+1]

        print(''.join(parentheses_set))