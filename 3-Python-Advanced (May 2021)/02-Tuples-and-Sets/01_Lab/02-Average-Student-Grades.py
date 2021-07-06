# 2.	Average Student Grades
# Write a program which reads names of students and their grades and adds them to the student record.
# On the first line you will receive the number of students – N. On the next N lines you will be receiving a student's
# name and his/ her grade.
# For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point
# in the format: "{student's name} -> {grade1} {grade2} … {gradeN} (avg: {average_grade}) ".
# The order in which we print the result does not matter.

def calculate_avg(iter): # iter because it can be list, tuple, set, etc.
    avg = sum(iter) / len(iter)
    return f"{avg:.2f}"

N = int(input())

students = {}

for _ in range(N):
    student, grade = input().split()

    if student not in students:
        students[student] = [float(grade)]
    else:
        students[student].append(float(grade))

for s, g in students.items():
    s_average = calculate_avg(g)
    print(f"{s} ->", end = " ")
    for el in g:
        print(f"{el:.2f}", end = " ")
    print(f"(avg: {s_average})")