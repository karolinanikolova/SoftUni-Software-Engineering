# завръщане в миналото
# Иванчо е на 18 години и получава наследство, което се състои от X сума пари и машина на времето.
# Той решава да се върне до 1800 година, но не знае дали парите ще са достатъчни, за да живее без да работи.
# Напишете програма, която пресмята дали Иванчо ще има достатъчно пари, за да не се налага да работи до дадена година
# включително. Като приемем, че за всяка четна (1800, 1802 и т.н.) година ще харчи 12 000 долара. За всяка нечетна
# (1801, 1803 и т.н.) ще харчи 12 000 + 50 * [годините, които е навършил през дадената година].

inherited_money = float(input())
year_end_of_life = int(input())
current_age = 18
current_money = inherited_money

for year in range(1800, year_end_of_life + 1):
    if year % 2 == 0:
        current_money = current_money - 12000
    else:
        current_money = current_money - 12000 - 50 * (18 + year - 1800)

if current_money >= 0:
    print(f'Yes! He will live a carefree life and will have {current_money:.2f} dollars left.')
else:
    print(f'He will need {abs(current_money):.2f} dollars to survive.')