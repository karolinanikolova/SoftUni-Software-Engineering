# обръщение според възраст и пол
# Според въведени възраст (десетично число) и пол (m / f) да се отпечата обръщение:
#
# “Mr.” – мъж (пол “m”) на 16 или повече години.
# “Master” – момче (пол “m”) под 16 години.
# “Ms.” – жена (пол “f”) на 16 или повече години.
# “Miss” – момиче (пол “f”) под 16 години.

age = float(input())
sex = input()

if sex == 'f':
    if age >= 16:
        print('Ms.')
    elif age < 16:
        print('Miss')
elif sex == 'm':
    if age >= 16:
        print('Mr.')
    elif age < 16:
        print('Master')