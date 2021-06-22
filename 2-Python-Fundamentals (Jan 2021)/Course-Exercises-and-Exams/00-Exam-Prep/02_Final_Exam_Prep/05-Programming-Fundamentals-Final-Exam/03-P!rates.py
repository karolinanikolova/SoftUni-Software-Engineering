# Programming Fundamentals Final Exam 04.04.2020
# Problem 3. P!rates
#
# Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack… Daniels.
# Together with your comrades Jim (Beam) and Johnny (Walker) you have been roaming the seas, looking for gold and treasure… and the occasional killing, of course. Go ahead, target some wealthy settlements and show them the pirate`s way!
# Description
# Until the "Sail" command is given you will be receiving:
# •	Cities that you and your crew have targeted, with their population and gold, separated by "||".
# •	If you receive a city which has been already received, you have to increase the population and gold with the given values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
# •	"Plunder=>{town}=>{people}=>{gold}"
# o	You have successfully attacked and plundered the town, killing the given number of people and stealing the respective amount of gold.
# o	For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
# o	If any of those two values (population or gold) reaches zero, the town is disbanded.
# 	You need to remove it from your collection of targeted cities and print the following message: "{town} has been wiped off the map!"
# o	There will be no case of receiving more people or gold than there is in the city.
# •	"Prosper=>{town}=>{gold}"
# o	There has been a dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# o	The gold amount can be a negative number, so be careful. If a negative amount of gold is given print: "Gold added
# cannot be a negative number!" and ignore the command.
# o	If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the
# following message: "{gold added} gold added to the city treasury. {town} now has {total gold} gold."

command = input()

towns = {}

while not command == "Sail":
    town, people, gold = command.split("||")
    people = int(people)
    gold = int(gold)

    if town not in towns:
        towns[town] = {"people": people, "gold": gold}
    else:
        towns[town]["people"] += int(people)
        towns[town]["gold"] += int(gold)

    command = input()

event = input()

while not event == "End":
    if event.startswith("Plunder"):
        action, town, people, gold = event.split("=>")
        gold = int(gold)
        people = int(people)
        towns[town]["people"] -= people
        towns[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if towns[town]["people"] == 0 or towns[town]["gold"] == 0:
            towns.pop(town)
            print(f"{town} has been wiped off the map!")

    elif event.startswith("Prosper"):
        action, town, gold = event.split("=>")
        gold = int(gold)
        people = int(people)
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            gold_added = gold
            towns[town]["gold"] += gold_added
            print(f"{gold_added} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")

    event = input()

sorted_gold_descending_name_ascending = dict(sorted(towns.items(), key=lambda kvp: (-kvp[1]["gold"], kvp[0])))

if sorted_gold_descending_name_ascending:
    print(f"Ahoy, Captain! There are {len(sorted_gold_descending_name_ascending)} wealthy settlements to go to:")
    for town, people_and_gold in sorted_gold_descending_name_ascending.items():
        people = people_and_gold["people"]
        gold = people_and_gold["gold"]

        print(f"{town} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

