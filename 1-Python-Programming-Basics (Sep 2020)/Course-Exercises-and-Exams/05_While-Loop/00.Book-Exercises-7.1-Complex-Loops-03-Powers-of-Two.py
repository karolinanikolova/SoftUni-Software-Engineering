# числата от 1 до 2^n с for цикъл
# В следващия пример ще разгледаме ползването на обичайната стъпка с размер 1.
#
# Да се напише програма, която отпечатва числата от 1 до 2^n (две на степен n).
# Например, ако n = 10, то резултатът ще е 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024.

n = int(input())

for i in range (0, n + 1):
    print(2 ** i)