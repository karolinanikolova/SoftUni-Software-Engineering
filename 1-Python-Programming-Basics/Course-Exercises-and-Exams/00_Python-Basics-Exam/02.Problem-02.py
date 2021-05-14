# Задача 2. Процесори
# Да се напише програма, която  пресмята каква печалба или загуба ще реализира фирма произвеждаща AND процесори.
# Един процесор се изработва за 3 часа. Фирмата има даден брой служители, които работят определен брой дни.
# Приема се, че един служител работи 8 часа на ден. Фирмата има за цел да изработи определен брой процесори.
# Плануваният брой процесори, броят на служителите във фирмата и дните се прочитат от конзолата.
# Броят на произведените процесори да бъде закръглен към по-малкото цяло число.
#
# Пример: за 10 часа се изработват 10/3 = 3.33 процесора   3 процесора. Един брой струва 110.10 лв.
# Според количеството изработени процесори принтирайте на конзолата, колко повече или по-малко пари са изкарани
# от плануваното.

from math import floor

processors_needed = int(input())
count_workers = int(input())
count_workdays = int(input())

total_working_hours = count_workers * count_workdays * 8
processors_produced = floor(total_working_hours / 3)

if processors_produced >= processors_needed:
    print(f"Profit: -> {(processors_produced - processors_needed) * 110.10:.2f} BGN")
else:
    print(f"Losses: -> {(processors_needed - processors_produced) * 110.10:.2f} BGN")
