# 6. Balanced Parentheses
# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs
# after the former. There will be no interval symbols between the parentheses. You will be given three types of parentheses: (, {, and [.
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.

parentheses = input()
is_balanced = True
opening = []

mapper = {'{': '}', '[': ']', '(': ')'}

for p in parentheses:
    if p in "{[(":
        opening.append(p)
    else:
        if opening:
            current_opening_p = opening.pop()
            if not mapper[current_opening_p] == p:
                is_balanced = False
                break
        else:
            is_balanced = False

if is_balanced:
    print("YES")
else:
    print("NO")


# # Solution 2
# from collections import deque
#
# string = deque(input())
#
# stack = []
#
# is_balanced = True
#
# mapper = {'}': '{', ']': '[', ')': '('}
#
# while string:
#     string_first_character = string.popleft()
#     if string_first_character in "{[(":
#         stack.append(string_first_character)
#     else:
#         if stack:
#             stack_last_character = stack.pop()
#             if not mapper[string_first_character] == stack_last_character:
#                 is_balanced = False
#         else:
#             is_balanced = False
# if is_balanced:
#     print("YES")
# else:
#     print("NO")