# 5.	Игра на интервали
# Напишете програма, която да пресмята резултата от игра. Първо получавате число, което показва колко хода ще продължи
# играта. После за всеки ход на играта ще получавате по едно ново число. Според интервала в който попада числото се
# прибавят точки. Ако числото е отрицателно или по-голямо 50, тогава то е невалидно. В началото на играта резултата
# е 0 и на всеки ход се прибавят точки по следният начин:
# •	От 0 до 9  20 % от числото
# •	От 10 до 19  30 % от числото
# •	От 20 до 29  40 % от числото
# •	От 30 до 39  50 точки
# •	От 40 до 50  100 точки
# •	Невалидно число  резултата се дели на 2
# Освен резултата програмата трябва да изкарва статистика за проценти числа в дадените интервали.

count_total_rounds = int(input())
count_total_points = 0
count_points_0_9 = 0
count_points_10_19 = 0
count_points_20_29 = 0
count_points_30_39 = 0
count_points_40_50 = 0
count_points_invalid = 0

for i in range(1, count_total_rounds + 1):
    current_round_points = int(input())
    if 0 <= current_round_points < 10:
        count_total_points += current_round_points * 0.2
        count_points_0_9 += 1
    elif 10 <= current_round_points < 20:
        count_total_points += current_round_points * 0.3
        count_points_10_19 += 1
    elif 20 <= current_round_points < 30:
        count_total_points += current_round_points * 0.4
        count_points_20_29 += 1
    elif 30 <= current_round_points < 40:
        count_total_points += 50
        count_points_30_39 += 1
    elif 40 <= current_round_points <= 50:
        count_total_points += 100
        count_points_40_50 += 1
    else:
        count_total_points = count_total_points / 2
        count_points_invalid += 1

print(f'{count_total_points:.2f}')
print(f'From 0 to 9: {(count_points_0_9 / count_total_rounds) * 100:.2f}%')
print(f'From 10 to 19: {(count_points_10_19 / count_total_rounds) * 100:.2f}%')
print(f'From 20 to 29: {(count_points_20_29 / count_total_rounds) * 100:.2f}%')
print(f'From 30 to 39: {(count_points_30_39 / count_total_rounds) * 100:.2f}%')
print(f'From 40 to 50: {(count_points_40_50 / count_total_rounds) * 100:.2f}%')
print(f'Invalid numbers: {(count_points_invalid / count_total_rounds) * 100:.2f}%')