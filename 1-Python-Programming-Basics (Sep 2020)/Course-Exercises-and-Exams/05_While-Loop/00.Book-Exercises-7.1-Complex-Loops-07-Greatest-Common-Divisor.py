# Най-голям общ делител (НОД)
# Преди да продължим към следващата задача, е необходимо да се запознаем с определението за най-голям общ делител (НОД).
#
# Определение за НОД: най-голям общ делител на две естествени числа a и b е най-голямото число, което се дели
# едновременно и на a, и на b без остатък. Например:

a = int(input())
b = int(input())

while b != 0:
    old_b = b
    b = a % b
    a = old_b
print(a)