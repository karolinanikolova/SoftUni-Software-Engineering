# Problem 2. Mu Online
# You have initial health 100 and initial bitcoins 0. You will be given a string, representing the dungeons rooms.
# Each room is separated with '|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
# •	"potion"
# o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
# o	First print: "You healed for {amount} hp.".
# o	After that, print your current health: "Current health: {health} hp.".
# •	"chest"
# o	You've found some bitcoins, the number in the second part.
# o	Print: "You found {amount} bitcoins."
# •	In any other case you are facing a monster, you are going to fight. The second part of the room, contains the attack of the monster.
# You should remove the monster's attack from your health.
# o	If you are not dead (health <= 0) you've slain the monster, and you should print ("You slayed {monster}.")
# o	If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you`ve manage to reach: "Best room: {room}".
# If you managed to go through all the rooms in the dungeon, print on the next three lines:
# "You've made it!", "Bitcoins: {bitcoins}", "Health: {health}".

dungeon_rooms = input().split("|")

initial_health = 100
initial_bitcoins = 0

health = initial_health
bitcoins = initial_bitcoins
is_managed_all_rooms = True

for room_index in range(len(dungeon_rooms)):
    room = dungeon_rooms[room_index].split()
    command = room[0]
    number = int(room[1])

    if command == "potion":
        if health + number > initial_health:
            healed = initial_health - health
            health = initial_health
        else:
            healed = number
            health += number
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins += number

    else:
        health -= number
        monster = command
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_index + 1}")
            is_managed_all_rooms = False
            break

if is_managed_all_rooms:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

