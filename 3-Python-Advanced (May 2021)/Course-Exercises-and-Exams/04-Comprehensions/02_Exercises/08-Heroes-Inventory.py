# 8.	Heroes Inventory
# Using a comprehension, write a program that receives a hero's names and items that need to be added in their
# inventory (item name and item cost). Print the total amount of items with their total cost for each hero.

def update_heroes(name, names, item, price, heroes):

    if name not in names:
        return heroes

    if not heroes[name].get(item):
        heroes[name].update({item: int(price)})

    return heroes

names = input().split(', ')

data = input()

heroes = {name: {} for name in names}

while not data == "End":
    name, item, price = data.split('-')

    heroes = update_heroes(name, names, item, price, heroes)

    data = input()

print(*[f"{name} -> Items: {len(inventory)}, Cost: {sum([inventory[item] for item in inventory])}" for name, inventory in heroes.items()], sep='\n')
