# число от 1 до 9 на английски
# Да се изпише число в интервала от 1 до 9 с текст на английски език (числото се чете от конзолата).
# Можем да прочетем числото и след това чрез серия от проверки отпечатваме съответстващата му английска дума:

number = int(input())

if number == 1:
    print("one")
elif number == 2:
    print('two')
elif number == 3:
    print('three')
elif number == 4:
    print('four')
elif number == 5:
    print('five')
elif number == 6:
    print('six')
elif number == 7:
    print('seven')
elif number == 8:
    print('eight')
elif number == 9:
    print('nine')
else:
    print('number too big')