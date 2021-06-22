# 4.	Оценки
# Напишете програма, която да пресмята статистика на оценки от изпит.
# В началото програмата получава броят на студентите явили се на изпита и за всеки студент неговата оценка.
# На края програмата трябва да изпечата процента на студенти с оценка между 2.00 и 2.99, между 3.00 и 3.99,
# между 4.00 и 4.99, 5.00 или повече. Също така и средният успех на изпита.

student_count_total = int(input())
student_count_grade_2_3 = 0
student_count_grade_3_4 = 0
student_count_grade_4_5 = 0
student_count_grade_5_6 = 0
student_grade_total = 0

for student in range(1, student_count_total + 1):
    student_grade = float(input())
    student_grade_total += student_grade
    if 2.00 <= student_grade < 3.00:
        student_count_grade_2_3 += 1
    elif 3.00 <= student_grade < 4.00:
        student_count_grade_3_4 += 1
    elif 4.00 <= student_grade < 5.00:
        student_count_grade_4_5 += 1
    else:
        student_count_grade_5_6 += 1

print(f'Top students: {(student_count_grade_5_6 / student_count_total) * 100:.2f}%')
print(f'Between 4.00 and 4.99: {(student_count_grade_4_5 / student_count_total) * 100:.2f}%')
print(f'Between 3.00 and 3.99: {(student_count_grade_3_4 / student_count_total) * 100:.2f}%')
print(f'Fail: {(student_count_grade_2_3 / student_count_total) * 100:.2f}%')
print(f'Average: {(student_grade_total / student_count_total):.2f}')
