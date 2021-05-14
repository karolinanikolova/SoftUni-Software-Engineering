# 5.	Монети
# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко монети може
# да стане това.

# # Without while
# sum = float(input())
# counter_of_coins = 0
# sum = int(sum * 100)
#
# counter_of_coins += sum // 200
# sum = sum % 200
# counter_of_coins += sum // 100
# sum = sum % 100
# counter_of_coins += sum // 50
# sum = sum % 50
# counter_of_coins += sum // 20
# sum = sum % 20
# counter_of_coins += sum // 10
# sum = sum % 10
# counter_of_coins += sum // 5
# sum = sum % 5
# counter_of_coins += sum // 2
# sum = sum % 2
#
# if sum == 1:
#     counter_of_coins += 1
#
# print(int(counter_of_coins))

# With while
sum = float(input())
sum = int(sum * 100)
coin_type = 200
total_counter_of_coins = 0

while sum != 0:
    counter_of_coins = sum // coin_type
    total_counter_of_coins += counter_of_coins
    sum = sum % coin_type
    coin_type = coin_type // 2
    if coin_type == 25:
        coin_type = 20

print(int(total_counter_of_coins))

