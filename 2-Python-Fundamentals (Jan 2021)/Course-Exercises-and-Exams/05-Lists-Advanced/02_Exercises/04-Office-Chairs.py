# 4.	Office Chairs
# So you've found a meeting room - phew! ' \
#       'You arrive there ready to present, and find that someone has taken one or more of the chairs!! ' \
#       'You need to find some quick.... check all the other meeting rooms to see if all of the chairs are in use.
# You will be given a number n representing how many rooms there are.
# On the next n lines for each room you will get how many chairs there are and how many of them will be taken.
# The chairs will be represented by "X"s, then there will be a space " " and a number representing the taken places.
# Example: "XXXXX 4" (5 chairs and 1 of them is left free). Keep track of the free chairs, you will need them later.
# However if you get to a room where there are more people than chairs, print the following message:
# "{needed_chairs_in_room} more chairs needed in room {number_of_room}". If there is enough chairs in each room print: \
#     "Game On, {total_free_chairs} free chairs left"

# rooms_count = int(input())
#
# free_chairs_in_each_room = []
# enough_chairs_in_each_room = True
#
# for room in range(1, rooms_count + 1):
#     room_chairs = input().split()
#     free_chairs_in_room = len(room_chairs[0]) - int(room_chairs[1])
#     if free_chairs_in_room < 0:
#         print(f"{abs(free_chairs_in_room)} more chairs needed in room {room}")
#         enough_chairs_in_each_room = False
#     else:
#         free_chairs_in_each_room.append(free_chairs_in_room)
#
# if enough_chairs_in_each_room:
#     print(f"Game On, {sum(free_chairs_in_each_room)} free chairs left")

rooms_count = int(input())

free_chairs_in_each_room = []
enough_chairs_in_each_room = True

for room in range(1, rooms_count + 1):
    room_chairs, n_people = input().split()
    free_chairs_in_room = len(room_chairs) - int(n_people)
    if free_chairs_in_room < 0:
        print(f"{abs(free_chairs_in_room)} more chairs needed in room {room}")
        enough_chairs_in_each_room = False
    else:
        free_chairs_in_each_room.append(free_chairs_in_room)

if enough_chairs_in_each_room:
    print(f"Game On, {sum(free_chairs_in_each_room)} free chairs left")