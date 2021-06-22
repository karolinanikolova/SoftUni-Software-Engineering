# 7.	Футболен турнир
# Екипът на СофтУни си организира футболен турнир. Първоначално прочитаме от конзолата капацитета на стадиона и
# броят на всички фенове. След това за всеки фен се чете секторът, в който се намира. Феновете на първия отбор са в
# сектор А и Б, а на втория – В и Г. Да се напише програма, която изчислява процентите на феновете във всеки сектор,
# спрямо общия брой фенове на стадиона, както и общият процент на феновете за двата отбора, спрямо капацитета на стадиона.
# Общият брой на феновете НЕ надвишава капацитета на стадиона.

stadium_capacity = int(input())
count_fans_total = int(input())
count_fans_sector_A = 0
count_fans_sector_B = 0
count_fans_sector_V = 0
count_fans_sector_G = 0

for fan in range(1, count_fans_total + 1):
    current_fan_sector = input()
    if current_fan_sector == 'A':
        count_fans_sector_A += 1
    elif current_fan_sector == 'B':
        count_fans_sector_B += 1
    elif current_fan_sector == 'V':
        count_fans_sector_V += 1
    elif current_fan_sector == 'G':
        count_fans_sector_G += 1

print(f'{(count_fans_sector_A / count_fans_total) * 100:.2f}%')
print(f'{(count_fans_sector_B / count_fans_total) * 100:.2f}%')
print(f'{(count_fans_sector_V / count_fans_total) * 100:.2f}%')
print(f'{(count_fans_sector_G / count_fans_total) * 100:.2f}%')
print(f'{((count_fans_sector_A + count_fans_sector_B + count_fans_sector_V + count_fans_sector_G) / stadium_capacity) * 100:.2f}%')