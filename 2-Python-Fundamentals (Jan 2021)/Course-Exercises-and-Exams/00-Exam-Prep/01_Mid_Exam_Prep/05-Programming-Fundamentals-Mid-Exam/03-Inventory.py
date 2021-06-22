# Problem 3. Inventory
# As a young traveler, you gather items and craft new items.
# Input / Constraints
# You will receive a journal with some Collecting items, separated with ', ' (comma and space).
# After that, until receiving "Craft!" you will be receiving different commands.
# Commands (split by " - "):
# •	"Collect - {item}" – Receiving this command, you should add the given item in your inventory.
# If the item already exists, you should skip this line.
# •	"Drop - {item}" – You should remove the item from your inventory, if it exists.
# •	"Combine Items - {oldItem}:{newItem}" – You should check if the old item exists, if so, add the new item after the old one.
# Otherwise, ignore the command.
# •	"Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.

def check_if_item_exists(items_list, item_to_check):
    if item_to_check in items_list:
        return True
    return False


def add_item(items_list, item_to_check):
    if not check_if_item_exists(items_list, item_to_check):
        items_list.append(item)
    return items_list


def remove_item(items_list, item_to_check):
    if check_if_item_exists(items_list, item_to_check):
        items_list.remove(item)
    return items_list


def combine_item(items_list, items_to_check):
    old_item, new_item = items_to_check.split(":")

    if check_if_item_exists(items_list, old_item):
        old_item_index = items_list.index(old_item)
        new_item_index = old_item_index + 1
        items_list.insert(new_item_index, new_item)
    return items_list


def renew_item(items_list, item_to_check):
    if check_if_item_exists(items_list, item_to_check):
        items_list.remove(item)
        items_list.append(item)
    return items_list


inventory = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")
    action = command[0]

    if action == 'Collect':
        item = command[1]
        inventory = add_item(inventory, item)

    elif action == 'Drop':
        item = command[1]
        inventory = remove_item(inventory, item)

    elif action == 'Combine Items':
        items = command[1]
        inventory = combine_item(inventory, items)

    elif action == 'Renew':
        item = command[1]
        inventory = renew_item(inventory, item)

    command = input()

# print(", ".join(inventory))
print(*inventory, sep=", ")

