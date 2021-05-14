# 8.	*Стипендии
# Учениците могат да кандидатстват за социална стипендия или за стипендия за отличен успех.
# Изискване за социална стипендия - доход на член от семейството по-малък от минималната работна заплата и успех над 4.5.
# Размер на социалната стипендия - 35% от минималната работна заплата. Изискване за стипендия за отличен успех - успех над 5.5, включително.
# Размер на стипендията за отличен успех - успехът на ученика, умножен по коефициент 25.
# Напишете програма, която при въведени доход, успех и минимална работна заплата, дава информация дали ученик има право да получава стипендия,
# и стойността на стипендията, която е по-висока за него.

from math import floor

income = float(input())
grade = float(input())
min_salary = float(input())

social_scholarship = min_salary * 0.35
excellence_scholarship = grade * 25

if grade <= 4.5:
    print(f'You cannot get a scholarship!')
elif grade >= 5.5:
    if income < min_salary:
        if excellence_scholarship >= social_scholarship:
            print(f'You get a scholarship for excellent results {floor(excellence_scholarship)} BGN')
        else:
            print(f'You get a Social scholarship {floor(social_scholarship)} BGN')
    else:
        print(f'You get a scholarship for excellent results {floor(excellence_scholarship)} BGN')
else:
    if income < min_salary:
        print(f'You get a Social scholarship {floor(social_scholarship)} BGN')
    else:
        print(f'You cannot get a scholarship!')

## Other method
# from math import floor
#
# income = float(input())
# grade = float(input())
# min_salary = float(input())
#
# social_scholarship = 0
# excellence_scholarship = 0
#
# # var = {excellence_scholarship:'scholarship for excellent results', social_scholarship:'Social scholarship'}
#
# if income < min_salary:
#     social_scholarship = 0.35 * min_salary
#
# if grade <= 4.5:
#     print(f'You cannot get a scholarship!')
# elif grade >= 5.5:
#     excellence_scholarship = grade * 25
#     if excellence_scholarship - social_scholarship == 0:
#         print(f'You get a scholarship for excellent results {floor(excellence_scholarship)} BGN')
#     elif excellence_scholarship - social_scholarship > 0:
#         print(f'You get a scholarship for excellent results {floor(excellence_scholarship)} BGN')
#     else:
#         print(f'You get a Social scholarship {floor(social_scholarship)} BGN')
# else:
#     if income < min_salary:
#         print(f'You get a Social scholarship {floor(social_scholarship)} BGN')
#     else:
#         print(f'You cannot get a scholarship!')




