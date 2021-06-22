# 3.	Elevator
# Calculate how many courses will be needed to elevate n persons by using an elevator with capacity of p persons.
# The input holds two lines: the number of people n and the capacity p of the elevator.

from math import ceil

number_of_people = int(input())
capacity = int(input())

courses = ceil(number_of_people / capacity)

print(courses)
