# amentals Mid Exam Retake 12 August 2020
# Problem 2. The Lift
# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it. If a wagon is full you should direct the people to the next one with space available.

people_waiting = int(input())

lift = [int(el) for el in input().split()]

max_people_in_lift = len(lift) * 4

for index in range(len(lift)):
    if lift[index] == 4:
        continue
    else:
        if people_waiting >= 4:
            people_to_add_to_wagon = 4 - lift[index]
        else:
            people_to_add_to_wagon = people_waiting
        lift[index] += people_to_add_to_wagon
        people_waiting -= people_to_add_to_wagon


if people_waiting == 0 and sum(lift) < max_people_in_lift:
    print("The lift has empty spots!")
    lift = [str(el) for el in lift]
    print(" ".join(lift))
elif people_waiting > 0 and sum(lift) == max_people_in_lift:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    lift = [str(el) for el in lift]
    print(" ".join(lift))
elif people_waiting == 0 and sum(lift) == max_people_in_lift:
    lift = [str(el) for el in lift]
    print(" ".join(lift))
