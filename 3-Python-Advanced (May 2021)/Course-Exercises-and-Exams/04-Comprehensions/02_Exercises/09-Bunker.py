# 9.	Bunker
# Using a comprehension, write a program that finds the number of given items in a bunker and their average quality.
# On the first line, you will be given all item categories present in the bunker, then you will be given a number (n).
# On the next "n" lines, you will be given different items in the following format:
# "{category} - {item_name} - quantity:{item_quantity};quality:{item_quality}"
# Store that information, you will need it later. After you receive all the inputs, print the total amount of items
# (sum the quantities) in the format:
# "Count of items: {count}"
# After that, print the average quality of all items in the following format, formatted to the second digit:
# "Average quality: {quality sum/categories count}"
# Finally, print all categories with the items on separate lines in the format:
# "{category} -> {item1}, {item2}, …".

categories = input().split(', ')

n = int(input())

storage = {category: [] for category in categories}

quantity = 0
quality = 0

for _ in range(n):
    category, item_name, quantity_and_quality = input().split(' - ')
    quantity += int(quantity_and_quality.split(';')[0].split(':')[1])
    quality += int(quantity_and_quality.split(';')[1].split(':')[1])

    storage[category].append(item_name)

print(f"Count of items: {quantity}")
print(f"Average quality: {quality/len(storage):.2f}")

[print(f"{category} -> {', '.join(item_names)}") for category, item_names in storage.items()]
