# 4.	Цена за транспорт
# Студент трябва да пропътува n километра. Той има избор измежду три вида транспорт:
# •	Такси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
# •	Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
# •	Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.
# Напишете програма, която въвежда броя километри n и период от деня (ден или нощ) и изчислява цената на най-евтиния транспорт.

n = int(input())
time = input()

if 0 < n < 20:
    if time == 'day':
        price = 0.70 + n * 0.79
    elif time == 'night':
        price = 0.70 + n * 0.90
elif 20 <= n < 100:
    if time == 'day':
        price = min([0.70 + n * 0.79, n * 0.09])
    elif time == 'night':
        price = min([0.70 + n * 0.90, n * 0.09])
elif n >= 100:
    if time == 'day':
        price = min([0.70 + n * 0.79, n * 0.09, n * 0.06])
    elif time == 'night':
        price = min([0.70 + n * 0.90, n * 0.09, n * 0.06])

print(f'{price:.2f}')