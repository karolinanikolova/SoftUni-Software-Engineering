# 4.	Число от 100 до 200
# Да се напише програма, която чете цяло число, въведено от потребителя, и проверява, дали е под 100, между 100 и 200 или над 200.
# Да се отпечатат съответно съобщения, като в примерите по-долу:

number = int(input())

if number < 100:
    print("Less than 100")
elif 100 <= number <= 200:
    print("Between 100 and 200")
elif number > 200:
    print("Greater than 200")