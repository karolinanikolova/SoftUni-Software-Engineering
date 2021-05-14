# 6.	Месечни разходи
# Напишете програма която да пресмята средният разход за месец на семейство за даден период време.
# За всеки месец разходите са следните:
# •	За ток – всеки месец е различен, ще се чете от конзолата
# •	за вода – 20 лв.
# •	за интернет – 15 лв.
# •	за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
# За всеки разход трябва да се пресметне колко общо е платено за всички месеци.

count_months_total = int(input())
monthly_bill_water = 20
monthly_bill_internet = 15
total_bill_water = monthly_bill_water * count_months_total
total_bill_internet = monthly_bill_internet * count_months_total
total_bill_electricity = 0
total_bill_other = 0

for month in range(1, count_months_total + 1):
    current_month_bill_electricity = float(input())
    current_month_bill_other = (monthly_bill_water + monthly_bill_internet + current_month_bill_electricity) * 1.2
    total_bill_electricity += current_month_bill_electricity
    total_bill_other += current_month_bill_other

print(f'Electricity: {total_bill_electricity:.2f} lv')
print(f'Water: {total_bill_water:.2f} lv')
print(f'Internet: {total_bill_internet:.2f} lv')
print(f'Other: {total_bill_other:.2f} lv')
print(f'Average: {(total_bill_electricity + total_bill_water + total_bill_internet + total_bill_other) / count_months_total:.2f} lv')
