# 3. Компютърна зала
# В най-голямата компютърна зала в България цените варират поради голямата посещаемост.
# Таксите на залата са в зависимост от това дали е ден или нощ, както и месецът,  в който се посещава залата. Цените са следните:
# 	Март до Май	Юни до Август
#  Ден	10.50 лв/ч	12.60 лв/ч
#  Нощ	8.40 лв/ч	10.20 лв/ч
# Предлагат се и следните отстъпки в следната последователност:
# •	За група от четирима или повече човека, цената на човек се намаля с 10%
# •	За 5 или повече часа прекарани, цената на човек се намаля с 50%
# Да се напише програма, която изчислява цената на човек за час и общата сума.

month = input()
hours_spent = int(input())
count_people_in_group = int(input())
time_of_day = input()

if time_of_day == 'day':
    if month == 'march' or month == 'april' or month == 'may':
        price_per_person_per_hour = 10.50
    elif month == 'june' or month == 'july' or month == 'august':
        price_per_person_per_hour = 12.60
elif time_of_day == 'night':
    if month == 'march' or month == 'april' or month == 'may':
        price_per_person_per_hour = 8.40
    elif month == 'june' or month == 'july' or month == 'august':
        price_per_person_per_hour = 10.20

if count_people_in_group >= 4:
    price_per_person_per_hour = 0.9 * price_per_person_per_hour

if hours_spent >= 5:
    price_per_person_per_hour = 0.5 * price_per_person_per_hour

total_cost = price_per_person_per_hour * count_people_in_group * hours_spent

print(f"Price per person for one hour: {price_per_person_per_hour:.2f}")
print(f"Total cost of the visit: {total_cost:.2f}")
