# магазин за плодове
# Магазин за плодове в работни дни продава на следните цени:
#
# Напишете програма, която чете от конзолата плод (banana / apple / …), ден от седмицата (Monday / Tuesday / …) и
# количество (десетично число) и пресмята цената според цените от таблиците по-горе. Резултатът да се отпечата закръглен
# с 2 цифри след десетичния знак. При невалиден ден от седмицата или невалидно име на плод да се отпечата “error”.

fruit = input()
day_of_week = input()
quantity = float(input())
price = 0
is_valid = True

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
    else:
        is_valid = False
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
    else:
        is_valid = False
else:
    is_valid = False

sum = price * quantity

if is_valid == True:
    print(f'{sum:.2f}')
elif is_valid == False:
    print('error')