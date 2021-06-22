# 5.	Фирма
# Фирма получава заявка за изработването на проект, за който са необходими определен брой часове.
# Фирмата разполага с определен брой дни. През 10% от дните служителите са на обучение и не могат да работят по проекта.
# Един нормален работен ден във фирмата е 8 часа. Всеки служител може да работи по проекта в извънработно време по 2 часа на ден.
# Часовете трябва да са закръглени към по-ниско цяло число (Например –> 6.98 часа се закръглят на 6 часа).
# Напишете програма, която изчислява дали фирмата може да завърши проекта навреме и колко часа не достигат или остават.

from math import floor

hours_needed = int(input())
days_available = int(input())
count_crazy_workers = int(input())

hours_available = floor(days_available * 8 * 0.9 + days_available * count_crazy_workers * 2)

if hours_available >= hours_needed:
    print(f'Yes!{hours_available - hours_needed} hours left.')
elif hours_available < hours_needed:
    print(f'Not enough time!{hours_needed - hours_available} hours needed.')
