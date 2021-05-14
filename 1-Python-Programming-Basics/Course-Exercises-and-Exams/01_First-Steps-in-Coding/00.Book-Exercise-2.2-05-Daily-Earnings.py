# дневна печалба
# Иван е програмист в американска компания и работи от вкъщи средно N дни в месеца, като изкарва средно по M долара на ден.
# В края на годината Иван получава бонус, който е равен на 2.5 месечни заплати.
# От спечеленото през годината му се удържат 25% данъци.
# Напишете програма, която да пресмята колко е чистата средна печалба на Иван на ден в лева, тъй като той харчи изкараното в България.
# Приема се, че в годината има точно 365 дни. Курсът на долара спрямо лева ще се подава на функцията.

N = int(input())
M = float(input())
USD_to_BGN = float(input())
tax = 0.25

monthly_earnings = M * N

bonus = monthly_earnings * 2.5

earnings_total = (monthly_earnings * 12 + bonus) * (1 - tax)
earnings_total_BGN = earnings_total * USD_to_BGN

earnings_total_BGN_per_day = earnings_total_BGN / 365

print(f"{earnings_total_BGN_per_day:.2f}")


