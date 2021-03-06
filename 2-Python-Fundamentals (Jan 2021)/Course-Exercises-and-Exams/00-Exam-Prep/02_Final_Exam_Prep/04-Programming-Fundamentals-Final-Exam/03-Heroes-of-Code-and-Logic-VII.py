# Problem 3. Heroes of Code and Logic VII
# You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic.
# You want to play it all day long! So cancel all other arrangements and create your party!
#
# On the first line of the standard input you will receive an integer n – the number of heroes that you can choose
# for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated
# by empty space in the following format:
# {hero name} {HP} {MP}
# -	where HP stands for hit points and MP for mana points
# -	a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game.  You will be receiving different
# commands, each on a new line, separated by " – ", until the "End" command is given.
# There are several actions that can be performed by the heroes:
# CastSpell – {hero name} – {MP needed} – {spell name}
# •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
# o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# •	If the hero is unable to cast the spell print:
# o	"{hero name} does not have enough MP to cast {spell name}!"
# TakeDamage – {hero name} – {damage} – {attacker}
# •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
# o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# •	If the hero has died, remove him from your party and print:
# o	"{hero name} has been killed by {attacker}!"
# Recharge – {hero name} – {amount}
# •	The hero increases his MP. If a command is given that would bring the MP of the hero above the maximum value (200),
# MP is increased to 200. (the MP can’t go over the maximum value).
# •	 Print the following message:
# o	"{hero name} recharged for {amount recovered} MP!"
# Heal – {hero name} – {amount}
# •	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100),
# HP is increased to 100 (the HP can’t go over the maximum value).
# •	 Print the following message:
# o	"{hero name} healed for {amount recovered} HP!"

n = int(input())

heroes = {}

for _ in range(n):
    hero_name, HP, MP = input().split()
    HP = int(HP)
    MP = int(MP)

    heroes[hero_name] = {"HP": HP, "MP": MP}

command = input()

while not command == "End":
    command = command.split(" - ")
    action = command[0]

    if action == "CastSpell":
        hero_name = command[1]
        MP_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name]["MP"] >= MP_needed:
            heroes[hero_name]["MP"] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]

        heroes[hero_name]["HP"] -= damage
        if heroes[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif action == "Recharge":
        hero_name = command[1]
        MP_to_be_added = int(command[2])
        if heroes[hero_name]["MP"] + MP_to_be_added > 200:
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['MP']} MP!")
            heroes[hero_name]["MP"] = 200
        else:
            heroes[hero_name]["MP"] += MP_to_be_added
            print(f"{hero_name} recharged for {MP_to_be_added} MP!")

    elif action == "Heal":
        hero_name = command[1]
        HP_to_be_added = int(command[2])
        if heroes[hero_name]["HP"] + HP_to_be_added > 100:
            print(f"{hero_name} healed for {100 - heroes[hero_name]['HP']} HP!")
            heroes[hero_name]["HP"] = 100
        else:
            heroes[hero_name]["HP"] += HP_to_be_added
            print(f"{hero_name} healed for {HP_to_be_added} HP!")

    command = input()

heroes_sorted_HP_descending_names_ascending = dict(sorted(heroes.items(), key=lambda kvp:(-kvp[1]["HP"], kvp[0])))

for hero_name, HP_and_MP in heroes_sorted_HP_descending_names_ascending.items():
    HP = HP_and_MP["HP"]
    MP = HP_and_MP["MP"]
    print(hero_name)
    print(f"  HP: {HP}")
    print(f"  MP: {MP}")
