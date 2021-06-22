# числа на Фибоначи
# Числата на Фибоначи в математиката образуват редица, която изглежда по следния начин: 1, 1, 2, 3, 5, 8, 13, 21, 34, ….
#
# Формулата за образуване на редицата е:
# F0 = 1
# F1 = 1
# Fn = Fn-1 + Fn-2
#
# Да се въведе цяло число n и да се пресметне n-тото число на Фибоначи.

n = int(input())
last_number = 1
current_number = 1

for i in range(0, n - 1):
        next_number = last_number + current_number
        last_number = current_number
        current_number = next_number

print(current_number)

