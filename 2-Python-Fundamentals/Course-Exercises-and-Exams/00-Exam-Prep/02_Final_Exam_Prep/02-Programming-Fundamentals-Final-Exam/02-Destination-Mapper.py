# Programming Fundamentals Final Exam 09.08.2020
# Problem 2. Destination Mapper
# Now that you have planned out your tour, you are ready to go! Your next task is to mark all the points on the map that you are going to visit.
# You will be given a string representing some places on the map. You have to filter only the valid ones. A valid location is:
# •	Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
# •	After the first "=" or "/" there should be only letters (the first must be upper-case)
# •	The letters must be at least 3
# Example: In the string "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" only the first two locations are valid.
# After you have matched all the valid locations, you have to calculate travel points.
# They are calculated by summing the lengths of all the valid destinations that you have found on the map.
# At the end, on the first line print the following: "Destinations: {destinations joined by ', '}".
# On the second line print "Travel Points: {travel_points}".

# Solution 1
# import re
#
# string = input()
#
# pattern = r"(=|/)[A-Z][A-Za-z]{2,}\1"
#
# matches = [obj.group() for obj in re.finditer(pattern, string)]
# matches = [el[1:-1] for el in matches]
# length_of_matches = [len(el) for el in matches]
#
# print(f"Destinations: {', '.join(matches)}")
# print(f"Travel Points: {sum(length_of_matches)}")

# Solution 2
import re

string = input()

pattern = r"(?<=(/|=))[A-Z][a-zA-Z]{2,}(?=\1)"

matches = [obj.group() for obj in re.finditer(pattern, string)]
travel_points = sum([len(el) for el in matches])

print(f"Destinations: {', '.join(matches)}")
print(f"Travel Points: {travel_points}")


# # Solution 3
# import re
#
# string = input()
#
# pattern = r"(=|/)(?P<dest>[A-Z][A-Za-z]{2,})\1"
#
# destinations = []
# travel_points = 0
#
# for match in re.finditer(pattern, string):
#     destinations.append(match.group('dest'))
#     travel_points += len(match.group('dest'))
#
# print(f"Destinations: {', '.join(destinations)}")
# print(f"Travel Points: {travel_points}")