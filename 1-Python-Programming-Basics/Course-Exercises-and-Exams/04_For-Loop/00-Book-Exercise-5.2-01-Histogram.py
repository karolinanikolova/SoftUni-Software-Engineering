# хистограма
# Дадени са n цели числа в интервала [1 … 1000]. От тях някакъв процент p1 са под 200, процент p2 са от 200 до 399,
# процент p3 са от 400 до 599, процент p4 са от 600 до 799 и останалите p5 процента са от 800 нагоре.
# Да се напише програма, която изчислява и отпечатва процентите p1, p2, p3, p4 и p5.
#
# Пример: имаме n = 20 числа: 53, 7, 56, 180, 450, 920, 12, 7, 150, 250, 680, 2, 600, 200, 800, 799, 199, 46, 128, 65.
# Получаваме следното разпределение и визуализация:

n = int(input())
count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

for i in range(1, n + 1):
    current_number = int(input())
    if current_number < 200:
        count_p1 += 1
    elif 200 <= current_number <= 399:
        count_p2 += 1
    elif 400 <= current_number <= 599:
        count_p3 += 1
    elif 600 <= current_number <= 799:
        count_p4 += 1
    else:
        count_p5 += 1

p1 = (count_p1 / n) * 100
p2 = (count_p2 / n) * 100
p3 = (count_p3 / n) * 100
p4 = (count_p4 / n) * 100
p5 = (count_p5 / n) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
