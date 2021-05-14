# реколта
# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино. От 1 кв.м. лозе се изкарват Y килограма грозде.
# За 1 литър вино са нужни 2,5 кг. грозде. Желаното количество вино за продан е Z литра.
#
# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно.
# Ако е достатъчно, остатъкът се разделя по равно между работниците на лозето.

from math import ceil
from math import floor

area = int(input())
grape_per_area = float(input())
needed_wine = int(input())
count_workers = int(input())

grape = (0.4 * area * grape_per_area)
wine = grape / 2.5

if wine < needed_wine:
    print(f'It will be a tough winter! More {floor(needed_wine - wine)} liters wine needed.')
elif wine >= needed_wine:
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(wine - needed_wine)} liters left -> {ceil((wine - needed_wine) / count_workers)} liters per person.')
