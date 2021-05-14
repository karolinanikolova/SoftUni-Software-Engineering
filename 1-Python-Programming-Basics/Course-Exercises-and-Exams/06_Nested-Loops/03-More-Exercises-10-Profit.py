# 10.	Банкноти и монети
# Имаме банкноти и монети по 1лв., по 2лв. и по 5лв. Да се напише програма, която прочита въведените от потребителя
# брой банкноти и монети и сума, и извежда на екран всички възможни начини по които сумата може да се изплати с
# наличните банкноти.

max_counter_1_lv = int(input())
max_counter_2_lv = int(input())
max_counter_5_lv = int(input())
sum = int(input())

for count_1_lv in range(0, max_counter_1_lv + 1):
    for count_2_lv in range(0, max_counter_2_lv + 1):
        for count_5_lv in range(0, max_counter_5_lv + 1):
            if count_1_lv * 1 + count_2_lv * 2 + count_5_lv * 5 == sum:
                print(f"{count_1_lv} * 1 lv. + {count_2_lv} * 2 lv. + {count_5_lv} * 5 lv. = {sum} lv.")