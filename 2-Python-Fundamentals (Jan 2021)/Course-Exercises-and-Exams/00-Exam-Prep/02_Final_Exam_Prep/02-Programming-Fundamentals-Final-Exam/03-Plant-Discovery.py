# Programming Fundamentals Final Exam 09.08.2020
# Problem 3. Plant Discovery
# You have now returned from your world tour. On your way you have discovered some new plants and you want to gather
# some information about them and create an exhibition to see which plant is highest rated.
# On the first line you will receive a number n. On the next n lines, you will be given some information about the plants
# that you have discovered in the format: "{plant}<->{rarity}". Store that information, because you will need it later.
# If you receive a plant more than once, update its rarity.
# After that until you receive the command "Exhibition" you will be given some of these commands:
# •	Rate: {plant} - {rating} – add the given rating to the plant (store all ratings)
# •	Update: {plant} - {new_rarity} – update the rarity of the plant with the new one
# •	Reset: {plant} – remove all the ratings of the given plant
# Note: If any of the command is invalid, print "error"
# After the command "Exhibition" print the information that you have about the plants in the following format:
# Plants for the exhibition:
# - {plant_name}; Rarity: {rarity}; Rating: {average_rating formatted to the 2nd digit}
# …
# The plants should be sorted by rarity descending, then by average rating descending

# # Solution 1
# n = int(input())
#
# plants = {}
#
# for _ in range(n):
#     plant, rarity = input().split("<->")
#     rarity = float(rarity)
#     plants[plant] = {"rarity": rarity, "rating": []}
#
# command = input()
#
# while not command == "Exhibition":
#     command, command_parameters = command.split(": ")
#     action = command
#     command_parameters = command_parameters.split(" - ")
#     plant = command_parameters[0]
#     if plant in plants:
#         if action == "Rate":
#
#             rating = float(command_parameters[1])
#             plants[plant]["rating"].append(rating)
#
#         elif action == "Update":
#             rarity = float(command_parameters[1])
#             plants[plant]["rarity"] = rarity
#
#         elif action == "Reset":
#             plants[plant]["rating"] = []
#     else:
#         print("error")
#
#     command = input()
#
# # for rarity_and_rating in plants.values():
# #     rating = rarity_and_rating["rating"]
# #     if rating:
# #         rating = sum(rating) / len(rating)
# #     rarity_and_rating["rating"] = rating
#
# for plant, value in plants.items():
#     if value["rating"]:
#         average = sum(value["rating"]) / len(value["rating"])
#     else:
#         average = 0
#     plants[plant]['average'] = average
#
# # For numbers we can also sort descending with a "-" in front of kvp
# # sorted_plants_rarity_descending_rating_descending = dict(sorted(plants.items(), key=lambda kvp:(kvp[1]["rarity"], kvp[1]["average"]), reverse=True))
# sorted_plants_rarity_descending_rating_descending = dict(sorted(plants.items(), key=lambda kvp:(kvp[1]["rarity"], kvp[1]["average"]), reverse=True))
#
# print("Plants for the exhibition:")
# for plant, value in sorted_plants_rarity_descending_rating_descending.items():
#     average = value["average"]
#     rarity = value["rarity"]
#     print(f"- {plant}; Rarity: {round(rarity)}; Rating: {average:.2f}")


n = int(input())

plants = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    rarity = float(rarity)
    plants[plant] = {"rarity": rarity, "rating": []}

command = input()

while not command == "Exhibition":
    command, command_parameters = command.split(": ")
    action = command
    command_parameters = command_parameters.split(" - ")
    plant = command_parameters[0]
    try:
        if action == "Rate":

            rating = float(command_parameters[1])
            plants[plant]["rating"].append(rating)

        elif action == "Update":
            rarity = float(command_parameters[1])
            plants[plant]["rarity"] = rarity

        elif action == "Reset":
            plants[plant]["rating"] = []
    except KeyError:
        print("error")

    command = input()

# for rarity_and_rating in plants.values():
#     rating = rarity_and_rating["rating"]
#     if rating:
#         rating = sum(rating) / len(rating)
#     rarity_and_rating["rating"] = rating

for plant, value in plants.items():
    if value["rating"]:
        average = sum(value["rating"]) / len(value["rating"])
    else:
        average = 0
    plants[plant]['average'] = average

# For numbers we can also sort descending with a "-" in front of kvp
# sorted_plants_rarity_descending_rating_descending = dict(sorted(plants.items(), key=lambda kvp:(kvp[1]["rarity"], kvp[1]["average"]), reverse=True))
sorted_plants_rarity_descending_rating_descending = dict(sorted(plants.items(), key=lambda kvp:(kvp[1]["rarity"], kvp[1]["average"]), reverse=True))

print("Plants for the exhibition:")
for plant, value in sorted_plants_rarity_descending_rating_descending.items():
    average = value["average"]
    rarity = value["rarity"]
    print(f"- {plant}; Rarity: {round(rarity)}; Rating: {average:.2f}")
