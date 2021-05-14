# търговски комисионни
# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите s:
#
# Напишете програма, която чете име на град (стринг) и обем на продажбите (десетично число) и изчислява размера на
# комисионната. Резултатът да се изведе закръглен с 2 десетични цифри след десетичния знак.
# При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

city = input()
sales = float(input())
is_valid = True

if city == 'Sofia':
    if 0 <= sales <= 500:
        comission = 0.05
    elif 500 < sales <= 1000:
        comission = 0.07
    elif 1000 < sales <= 10000:
        comission = 0.08
    elif sales > 10000:
        comission = 0.12
    else:
        is_valid = False
elif city == 'Varna':
    if 0 <= sales <= 500:
        comission = 0.045
    elif 500 < sales <= 1000:
        comission = 0.075
    elif 1000 < sales <= 10000:
        comission = 0.1
    elif sales > 10000:
        comission = 0.13
    else:
        is_valid = False
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        comission = 0.055
    elif 500 < sales <= 1000:
        comission = 0.08
    elif 1000 < sales <= 10000:
        comission = 0.12
    elif sales > 10000:
        comission = 0.145
    else:
        is_valid = False
else:
    is_valid = False

if is_valid == True:
    print(f'{sales * comission:.2f}')
elif is_valid == False:
    print('error')