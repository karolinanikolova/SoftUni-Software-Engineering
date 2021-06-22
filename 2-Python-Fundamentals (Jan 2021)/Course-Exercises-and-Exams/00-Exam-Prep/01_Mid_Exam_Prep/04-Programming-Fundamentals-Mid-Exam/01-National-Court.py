# Problem 1. National Court
# Every day thousands of people pass by the reception at "National Court" with various questions to ask and the employees
# have to help everyone by providing correct information and to answer all questions.
# There are 3 employees working on the reception all day long. Each of them can handle different number of people per hour.
# Your task is to calculate how much time it will take to answer all the questions of a given number of people.
# First you will receive 3 lines with integers, representing the count of people that each of the employee can help per hour.
# On the next line you will receive the total people count as a single integer.
# Every fourth hour all the employees have a one-hour break before they start working again.
# This is the only break they get because they don`t need rest and have no personal life.
# Calculate the time needed to answer all people`s questions and print it in the following format: "Time needed: {time}h."

employee_one_people_helped_per_hour = int(input())
employee_two_people_helped_per_hour = int(input())
employee_three_people_helped_per_hour = int(input())

people_left_to_help = int(input())

people_helped_per_hour = employee_one_people_helped_per_hour + employee_two_people_helped_per_hour + employee_three_people_helped_per_hour

total_hours = 0
hours_since_break = 0

while people_left_to_help > 0:
    total_hours += 1
    hours_since_break += 1
    people_left_to_help -= people_helped_per_hour
    if hours_since_break % 3 == 0 and people_left_to_help != 0:
        total_hours += 1
        hours_since_break = 0

print(f"Time needed: {total_hours}h.")

