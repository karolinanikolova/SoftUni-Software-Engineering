# 7.	Магазин за детски играчки
# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели, иска да отиде на екскурзия. Да се напише програма, която пресмята печалбата от поръчката.
# Цени на играчките:
# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът, прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

price_excursion = float(input())
count_puzzle = int(input())
count_dolls = int(input())
count_teddy_bear = int(input())
count_minion = int(input())
count_truck = int(input())

price_puzzle = 2.60
price_doll = 3
price_teddy_bear = 4.10
price_minion = 8.20
price_truck = 2

count_toys = count_puzzle + count_dolls + count_teddy_bear + count_minion + count_truck

profit = (count_puzzle * price_puzzle + count_dolls * price_doll + count_teddy_bear * price_teddy_bear + count_minion * price_minion + count_truck * price_truck)

if count_toys >= 50:
    profit = profit * (1 - 0.25)

profit_actual = profit * (1 - 0.1)

if profit_actual >= price_excursion:
    print(f'Yes! {(profit_actual - price_excursion):.2f} lv left.')
else:
    print(f'Not enough money! {abs(profit_actual - price_excursion):.2f} lv needed.')

