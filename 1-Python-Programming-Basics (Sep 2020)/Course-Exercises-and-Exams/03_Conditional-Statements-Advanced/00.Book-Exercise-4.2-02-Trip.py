# пътешествие
# Странно, но повечето хора си плануват от рано почивката. Млад програмист разполага с определен бюджет и
# свободно време в даден сезон.
#
# Напишете програма, която да приема на входа бюджета и сезона, а на изхода да изкарва къде ще почива
# програмистът и колко ще похарчи.
#
# Бюджетът определя дестинацията, а сезонът определя колко от бюджета ще бъде изхарчен. Ако е лято, ще
# почива на къмпинг, а зимата - в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел.
# Всеки къмпинг или хотел, според дестинацията, има собствена цена, която отговаря на даден процент от бюджета:
#
# При 100 лв. или по-малко – някъде в България.
# Лято – 30% от бюджета.
# Зима – 70% от бюджета.
# При 1000 лв. или по малко – някъде на Балканите.
# Лято – 40% от бюджета.
# Зима – 80% от бюджета.
# При повече от 1000 лв. – някъде из Европа.
# При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.

budget = float(input())
season = input()
money_spent = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        holiday_type = 'Camp'
        money_spent = 0.3 * budget
    elif season == 'winter':
        holiday_type = 'Hotel'
        money_spent = 0.7 * budget
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        holiday_type = 'Camp'
        money_spent = 0.4 * budget
    elif season == 'winter':
        holiday_type = 'Hotel'
        money_spent = 0.8 * budget
else:
    destination = 'Europe'
    holiday_type = 'Hotel'
    money_spent = 0.9 * budget

print(f'Somewhere in {destination}')
print(f'{holiday_type} - {money_spent:.2f}')
