# Problem 1. Bonus Scoring System
# Create a program that calculates bonus points for each student, for a certain course.
# On the first line, you are going to receive the count of the students for this course.
#     On the second line, you will receive the count of the lectures in the course.
#     Every course has an additional bonus. You are going to receive it on the third line.
#     On the next lines, you will be receiving the count of attendances for each student.
# The bonus is calculated with the following formula:
# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
# Find the student with the maximum bonus and print him/her, along with his attendances in the following format:
# "Max Bonus: {maxBonusPoints}."
# "The student has attended {studentAttendances} lectures."
# Round the bonus points at the end to the nearest bigger number.

# count_students = int(input())
# count_lectures = int(input())
# additional_bonus = int(input())
#
# bonuses = []
# attendances = []
#
# for _ in range(1, count_students + 1):
#     count_attendance = int(input())
#     attendances.append(count_attendance)
#     student_bonus = (count_attendance / count_lectures) * (5 + additional_bonus)
#     bonuses.append(student_bonus)
#
# max_bonus = max(bonuses)
# index_of_max_bonus = bonuses.index(max_bonus)
# attendance_of_max_bonus = attendances[index_of_max_bonus]
#
# print(f"Max Bonus: {round(max_bonus)}.")
# print(f"The student has attended {attendance_of_max_bonus} lectures.")

from math import ceil

count_students = int(input())
count_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
attendance_of_max_bonus = 0

for _ in range(1, count_students + 1):
    count_attendance = int(input())
    if count_lectures != 0:
        student_bonus = (count_attendance / count_lectures) * (5 + additional_bonus)
    if student_bonus >= max_bonus:
        max_bonus = student_bonus
        attendance_of_max_bonus = count_attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attendance_of_max_bonus} lectures.")


