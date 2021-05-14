# 3.	Josephus Permutation
# This problem takes its name by arguably the most important event in the life of the ancient historian Josephus:
# according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.
# Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a
# circle and proceeded to kill one man every three, until one last man was left (and that it was supposed to kill himself to end the act).
# Well, Josephus and another man were the last two and, as we now know every detail of the story,
# you may have correctly guessed that they didn't exactly follow through the original idea.
# You are now to create a program that prints a Josephus permutation, receiving two lines of code
# (the list itself (string with elements separated by a single space) and a number k) as if they were in a circle and counted out every k places until none remained.

soldiers = input().split()
soldiers = list(map(int, soldiers))

k = int(input())
initial_number_of_soldiers = len(soldiers)

removed_soldiers = []

for position in range(1, len(soldiers)+1):
    index = position * k - 1 - len(removed_soldiers)
    if index > len(soldiers):
        index = index % len(soldiers)
    removed_soldier = soldiers[index]
    removed_soldiers.append(removed_soldier)
    soldiers.remove(soldiers[index])
    count_soldiers_removed = len(removed_soldiers)

    print(removed_soldiers)