# Problem 1
# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal,
# you should make a milkshake and remove both ingredients. Otherwise you should move the cup of milk at the end of the
# sequence and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0, you should remove them from the records before trying to mix it with
# the other ingredient.
# When you successfully prepare 5 chocolate milkshakes or you have no more chocolate or cups of milk left, you need to
# stop making chocolate milkshakes.

from collections import deque

chocolate = [int(el) for el in input().split(', ')]
milk = deque([int(el) for el in input().split(', ')])

matches = 0

while chocolate and milk and matches != 5:
    is_time_for_next_turn = False
    current_chocolate = chocolate[-1]
    current_milk = milk[0]

    if current_milk <= 0:
        milk.popleft()
        is_time_for_next_turn = True

    if current_chocolate <= 0:
        chocolate.pop()
        is_time_for_next_turn = True

    if is_time_for_next_turn:
        continue

    if current_chocolate == current_milk:
        chocolate.pop()
        milk.popleft()
        matches += 1
        continue
    else:
        milk.append(milk.popleft())
        chocolate[-1] -= 5

if matches == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join(str(el) for el in chocolate)}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(str(el) for el in milk)}")
else:
    print("Milk: empty")

    should_continue = False

    if last_choko <= 0:
        cups_of_milk.appendleft(first_milk)
        should_continue = True
    if first_milk <= 0:
        chocolates.append(last_choko)
        should_continue = True

    if should_continue:
        continue