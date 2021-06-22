# 7.	 Student Academy
# Write a program that keeps information about students and their grades.
# You will receive n pair of rows. First you will receive the student's name, after that you will receive his grade.
# Check if the student already exists and if not, add him. Keep track of all grades for each student.
# When you finish reading the data, keep the students with average grade higher than or equal to 4.50.
# Order the filtered students by average grade in descending order.
# Print the students and their average grade in the following format:
# {name} –> {averageGrade}
# Format the average grade to the 2nd decimal place.

n = int(input())

students = {}

for _ in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

filtered_students_average_grades = {}

for student_name, grades in students.items():
    average_grade = sum(grades) / len(grades)

    if average_grade >= 4.50:
        if student_name not in filtered_students_average_grades:
            filtered_students_average_grades[student_name] = average_grade

sorted_remaining_students_average_grades = sorted(filtered_students_average_grades.items(), key=lambda kvp: kvp[1], reverse=True)

for student_name, average_grade in sorted_remaining_students_average_grades:
    print(f"{student_name} -> {average_grade:.2f}")
