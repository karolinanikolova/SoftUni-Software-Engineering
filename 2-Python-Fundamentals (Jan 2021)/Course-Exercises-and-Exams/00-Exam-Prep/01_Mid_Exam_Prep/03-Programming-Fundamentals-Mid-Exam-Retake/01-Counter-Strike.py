# Problem 1. Counter Strike
# Write a program that keeps track of every won battle against an enemy.
# You will receive initial energy.
# Afterwards you will start receiving the distance you need to go to reach an enemy until the "End of battle" command is given, or until you run out of energy.
# The energy you need for reaching an enemy is equal to the distance you receive.
# Each time you reach an enemy, your energy is reduced. This is considered a successful battle (win).
# If you don't have enough energy to reach an the enemy, print:
# "Not enough energy! Game ends with {count} won battles and {energy} energy"
# and end the program.
# Every third won battle increases your energy with the value of your current count of won battles.
# Upon receiving the "End of battle" command, print the count of won battles in the following format:
# "Won battles: {count}. Energy left: {energy}"

initial_energy = int(input())

command = input()

energy = initial_energy
count_won_battles = 0

while command != "End of battle" and initial_energy > 0:
    distance = int(command)
    if distance > energy:
        print(f"Not enough energy! Game ends with {count_won_battles} won battles and {energy} energy")
        break
    energy -= distance
    count_won_battles += 1
    if count_won_battles % 3 == 0:
        energy += count_won_battles
    command = input()

if command == "End of battle":
    print(f"Won battles: {count_won_battles}. Energy left: {energy}")
