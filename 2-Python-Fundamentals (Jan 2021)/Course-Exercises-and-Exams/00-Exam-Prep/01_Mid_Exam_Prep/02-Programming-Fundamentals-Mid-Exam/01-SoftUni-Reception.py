# 01.	 SoftUni Reception
# Every day thousands of students pass by the reception at SoftUni with different questions to ask and
# the employees have to help everyone by providing all the information and to answer all of the questions.
# There are 3 employees working on the reception all day. Each of them can handle different number of students per hour.
# Your task is to calculate how much time it will take to answer all the questions of given number of students.
# First you will receive 3 lines with integers, representing count of students that each of the employee can help per hour.
# On the next line you will receive students count as a single integer.
# Every forth hour all of the employees have a break, so they don’t work for a hour. This is the only break for the employees,
# because they don`t need rest, nor have a personal life. Calculate the time needed to answer all the student's ' \
# questions and print it in the following format: "Time needed: {time}h."

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

