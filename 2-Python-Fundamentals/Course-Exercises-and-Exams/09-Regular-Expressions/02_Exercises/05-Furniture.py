# 5.	Furniture
# Write a program to calculate the total cost of different types of furniture.
# You will be given some lines of input until you receive the line "Purchase". For the line to be valid it should be in the following format:
# ">>{furniture name}<<{price}!{quantity}"
# The price can be floating point number or whole number. Store the names of the furniture and the total price.
# At the end print the each bought furniture on separate line in the format:
# "Bought furniture:
# {1st name}
# {2nd name}
# …"
# And on the last line print the following: "Total money spend: {spend money}" formatted to the second decimal point.

import re

text = input()

pattern = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"

spent_money = 0
furniture_names = []

while not text == "Purchase":
    furniture = [match_obj.groupdict() for match_obj in re.finditer(pattern, text)]
    if furniture:
        spent_money += float(furniture[0]['price']) * float(furniture[0]['quantity'])
        furniture_names.append(furniture[0]['name'])
    text = input()


# while not text == "Purchase":
#     match = re.match(pattern, text)
#
#     if match:
#         data = match.groupdict()
#         furniture_names.append(data['name'])
#         spent_money += float(data['price']) * float(data['quantity'])
#
#     text = input()

print("Bought furniture:")
# if furniture_names:
#     print("\n".join(furniture_names))
[print(furniture) for furniture in furniture_names]
print(f"Total money spend: {spent_money:.2f}")
