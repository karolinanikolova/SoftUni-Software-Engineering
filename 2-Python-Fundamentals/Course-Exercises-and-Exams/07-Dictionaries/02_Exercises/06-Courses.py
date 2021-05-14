# 6.	Courses
# Write a program that keeps information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name, until you receive the command "end".
# Check if such course already exists, and if not, add the course. Register the user into the course.
# When you receive the command "end", print the courses with their names and total registered users, ordered by the
# count of registered users in descending order. For each contest print the registered users ordered by name in ascending order.

data = input()

courses = {}

while not data == "end":
    course_name, student_name = data.split(" : ")

    if course_name not in courses:
        courses[course_name] = {"student_names": [], "registered_users_count": 0}
    courses[course_name]["student_names"].append(student_name)
    courses[course_name]["registered_users_count"] += 1

    data = input()

courses_sorted_by_registered_users_descending = dict(sorted(courses.items(), key=lambda kvp: kvp[1]["registered_users_count"], reverse=True))

for course_name, values in courses_sorted_by_registered_users_descending.items():
    registered_users_count = values["registered_users_count"]
    student_names = values["student_names"]
    student_names.sort()

    print(f"{course_name}: {registered_users_count}")
    for student in student_names:
        print(f"-- {student}")
