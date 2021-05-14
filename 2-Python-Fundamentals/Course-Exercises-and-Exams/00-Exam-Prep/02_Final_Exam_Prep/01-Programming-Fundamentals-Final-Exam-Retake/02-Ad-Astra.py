# Programming Fundamentals Final Exam Retake 15.08.2020
# Problem 2. Ad Astra
# You are an astronaut who just embarked on a mission across the solar system. Since you will be in space for a long time,
# you have packed a lot of food with you. Create a program, which helps you  identify how much food you have left and gives
# you information about its expiration date.
# On the first line of the input you will be given a text string. You must extract the information about the food and calculate the total calories.
# First you must extract the food info. It will always follow the same pattern rules:
# •	It will be surrounded by "|" or "#" (only one of the two) in the following pattern:
# #{item name}#{expiration date}#{calories}#   or
# |{item name}|{expiration date}|{calories}|
# •	The item name will contain only lowercase and uppercase letters and whitespace
# •	The expiration date will always follow the pattern: {day}/{month}/{year}, where the day, month and year will be exactly two digits long
# •	The calories will be an integer between 0-10000
# Calculate the total calories of all food items and then determine how many days you can last with the food you have.
# Keep in mind that you need 2000kcal a day.

# Solution 1
import re

text = input()

pattern = r"(#|\|)(?P<name>[A-Za-z\s]+)\1(?P<day>[0-2][1-9]|[1-3]0|31)/(?P<month>0[1-9]|1[0-2])/(?P<year>\d{2})\1(?P<calories>[0-9]{1,4}|10000)\1"

food_data = [match.groupdict() for match in re.finditer(pattern, text)]

total_calories = 0

for food in food_data:
    total_calories += int(food["calories"])

print(f"You have food to last you for: {total_calories//2000} days!")

for food in food_data:
    print(f"Item: {food['name']}, Best before: {food['day']}/{food['month']}/{food['year']}, Nutrition: {food['calories']}")

# # Solution 2
# import re
#
# text = input()
#
# pattern = r"(#|\|)(?P<name>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9]{1,4}|10000)\1"
#
# matches = re.finditer(pattern, text)
# food_data = []
#
# total_calories = 0
#
# for match in matches:
#     object_dict = match.groupdict()
#     food_data.append(object_dict)
#     total_calories += int(object_dict['calories'])
#
# days = total_calories // 2000
#
# print(f"You have food to last you for: {days} days!")
#
# for food in food_data:
#     print(f"Item: {food['name']}, Best before: {food['date']}, Nutrition: {food['calories']}")


# # Solution 3
# import re
#
# text = input()
#
# pattern = r"(#|\|)(?P<name>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9]{1,4}|10000)\1"
#
# total_calories = 0
#
# for match in re.finditer(pattern, text):
#     calories = int(match.group('calories'))
#     total_calories += calories
#
# days = total_calories // 2000
# print(f"You have food to last you for: {days} days!")
#
# for match in re.finditer(pattern, text):
#     name = match.group('name')
#     date = match.group('date')
#     calories = match.group('calories')
#     print(f"Item: {name}, Best before: {date}, Nutrition: {calories}")
