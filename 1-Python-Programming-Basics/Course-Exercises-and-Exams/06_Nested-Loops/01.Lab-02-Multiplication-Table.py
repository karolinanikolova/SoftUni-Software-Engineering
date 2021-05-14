# 2.	Таблица за умножение
# Отпечатайте на конзолата таблицата за умножение за числата от 1 до 10 във формат:
# "{първи множител} * {втори множител} = {резултат}".

for first_multiplier in range(1, 11):
    for second_multiplier in range(1, 11):
        print(f'{first_multiplier} * {second_multiplier} = {first_multiplier * second_multiplier}')
