# 3.	Legendary Farming
# You've done all the work and the last thing left to accomplish is to own a legendary item.
# However, it's a tedious process and it requires quite a bit of farming. Anyway, you are not too pretentious –
# any legendary item will do. The possible items are:
# •	Shadowmourne – requires 250 Shards;
# •	Valanyr – requires 250 Fragments;
# •	Dragonwrath – requires 250 Motes;
# Shards, Fragments and Motes are the key materials and everything else is junk. You will be given lines of input, in the format:
# 2 motes 3 ores 15 stones
# Keep track of the key materials - the first one that reaches the 250 mark, wins the race.
# At that point you have to print that the corresponding legendary item is obtained.
# Then, print the remaining shards, fragments, motes, ordered by quantity in descending order,
# then by name in ascending order, each on a new line. Finally, print the collected junk items in alphabetical order.

data = input()

key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}

is_obtained = False

while not is_obtained:
    split_data = data.split()

    for index in range(0, len(split_data), 2):

        if is_obtained:
            break

        quantity = int(split_data[index])
        material = split_data[index+1].lower()

        if material in items:
            items[material] += quantity
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity

        for material, quantity in items.items():
            if quantity >= 250:
                is_obtained = True
                items[material] -= 250
                print(f"{key_materials[material]} obtained!")
                break

    if is_obtained:
        break

    data = input()

# For numbers we can also sort descending with a "-" in front of kvp. Or we use reverse = True if not numbers
sorted_items = sorted(items.items(), key=lambda kvp: (-kvp[1], kvp[0]))

for material, quantity in sorted_items:
    print(f"{material}: {quantity}")

sorted_junks = sorted(junk_items.items(), key=lambda kvp: kvp[0])

for material, quantity in sorted_junks:
    print(f"{material}: {quantity}")