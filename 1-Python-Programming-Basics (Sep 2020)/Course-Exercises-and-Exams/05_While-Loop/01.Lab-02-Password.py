# 2.	Парола
# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход,
# при въвеждане на грешна парола, потребителя да се подкани да въведе нова парола.

username = input()
password = input()

input_password = input()

while input_password != password:
    input_password = input()
else:
    print(f'Welcome {username}!')