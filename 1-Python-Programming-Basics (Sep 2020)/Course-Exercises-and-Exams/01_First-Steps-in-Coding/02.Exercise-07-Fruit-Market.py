# 7.	* Пазар за плодове
# Мария решава да мине на диета и отива до  близкия пазар, за да купи ягоди, банани, портокали и малини.
# Да се напише програма, която пресмята колко пари са  ѝ необходими за да плати сметката, като знаете, че:
# •	цената на  малините е на половина по-ниска от тази на ягодите;
# •	цената на портокалите е с 40% по-ниска от цената на малините;
# •	цената на бананите е с 80% по-ниска от цената на малините.

price_strawberries = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberries = float(input())
kg_strawberries = float(input())

price_raspberries = 0.5 * price_strawberries
price_oranges = 0.6 * price_raspberries
price_bananas = 0.2 * price_raspberries

price_total = price_bananas * kg_bananas + price_oranges * kg_oranges + price_raspberries * kg_raspberries + price_strawberries * kg_strawberries
print(price_total)