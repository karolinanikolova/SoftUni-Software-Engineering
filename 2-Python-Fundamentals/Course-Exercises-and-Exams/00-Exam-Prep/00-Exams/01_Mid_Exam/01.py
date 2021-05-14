from math import ceil

budget = float(input())
students = int(input())
price_flour_package = float(input())
price_single_egg = float(input())
price_single_apron = float(input())

free_flour_packages = students // 5

price = price_single_apron * ceil(students * 1.2) + price_single_egg * 10 * students + price_flour_package * (students - free_flour_packages)

if price <= budget:
    print(f"Items purchased for {price:.2f}$.")
else:
    print(f"{price-budget:.2f}$ more needed.")
