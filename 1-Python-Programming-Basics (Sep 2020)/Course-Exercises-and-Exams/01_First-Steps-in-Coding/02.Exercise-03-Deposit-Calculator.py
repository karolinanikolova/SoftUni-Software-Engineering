# 3.	Калкулатор депозити
# Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен процент. Използвайте следната формула:
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit_sum = float(input())
length_in_months = int(input())
annual_interest = float(input())

sum = deposit_sum + length_in_months * deposit_sum * annual_interest / 12 / 100
print(sum)