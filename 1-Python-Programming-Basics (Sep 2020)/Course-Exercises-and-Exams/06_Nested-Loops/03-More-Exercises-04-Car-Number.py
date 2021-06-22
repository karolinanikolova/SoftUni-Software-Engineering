# 4.	Номер
# Поздравления, поради вашите задълбочени знания в сферата на програмирането МВР реши да наеме точно вас за създаването
# на новата им система за генериране на специални автомобилни номера. Всеки един специален автомобилен номер се състой
# от четири числа. Условията, които разграничават специалните от обикновените номера са следните:
# •	Ако номерът започва с четна цифра, то той трябва да завършва на нечетна цифра и обратното – ако започва с нечетна,
# завършва на четна
# •	Първата цифра от номера е по-голяма от последната
# •	Сумата от втората и третата цифра трябва да е четно число
# Входа се състой от две числа - начало и край на интервал, между които трябва да се генерира всяко едно число от номера.

start_interval = int(input())
end_interval = int(input())

for first_number in range(start_interval, end_interval + 1):
    for second_number in range(start_interval, end_interval + 1):
        for third_number in range(start_interval, end_interval + 1):
            for fourth_number in range(start_interval, end_interval + 1):
                if (first_number + fourth_number) % 2 != 0 and first_number > fourth_number and (second_number + third_number) % 2 == 0:
                    print(f'{first_number}{second_number}{third_number}{fourth_number}', end= ' ')