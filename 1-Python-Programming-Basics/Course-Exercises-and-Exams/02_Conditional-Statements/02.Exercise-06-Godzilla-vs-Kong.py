# 6.	Годзила срещу Конг
# Снимките за дългоочаквания филм "Годзила срещу Конг" започват.
# Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли, дали предвидените средства са достатъчни за снимането на филма.
# За снимките  ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

budget = float(input())
count_extras = int(input())
price_clothing_per_extra = float(input())

decor = 0.1 * budget

if count_extras <= 150:
    cost = count_extras * price_clothing_per_extra + decor
else:
    cost = count_extras * price_clothing_per_extra * 0.9 + decor

if cost > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {cost - budget:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {abs(cost - budget):.2f} leva left.')
