# 4.	Задължителна литература
# За лятната ваканция в спикъка със задължителна литература на Жоро има определен брой книги, но Жоро предпочита да играе с приятели навън.
# Вашата задача е да помогнете на Жоро да изчисли колко часа на ден трябва да отделя, за да прочете необходимата литература, но и да прекарва максимално време навън.

page_number = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

hours_per_book = page_number / pages_per_hour
hours_per_day = hours_per_book / number_of_days

print(hours_per_day)