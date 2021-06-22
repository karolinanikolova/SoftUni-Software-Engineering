# 5.	Numbers Filter
# You will receive a single number n. On the next n lines you will receive integers.
# After that you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

n = int(input())

evens = []
odds = []
positives = []
negatives = []

for _ in range(n):
    current_number = int(input())
    if current_number % 2 == 0:
        evens.append(current_number)

    if current_number % 2 == 1:
        odds.append(current_number)

    if current_number < 0:
        negatives.append(current_number)

    if current_number >= 0:
        positives.append(current_number)

command = input()

if command == 'even':
    print(evens)
elif command == 'odd':
    print(odds)
elif command == 'positive':
    print(positives)
else:
    print(negatives)
