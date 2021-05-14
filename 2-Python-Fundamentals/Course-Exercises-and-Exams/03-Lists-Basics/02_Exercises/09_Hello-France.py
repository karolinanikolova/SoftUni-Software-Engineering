# 9.	* Hello, France
# The budget was enough to get Ali and her friends to Frankfurt and they have some money left, but their final aim
# is to go to France, which means that they will need more finances. They’ve decided to make profit by buying items on
# discount from the Thrift Shop and selling them for a higher price. You must help them.
# Create a program that calculates the profit after buying some items and selling them on a higher price.
# In order to fulfil that, you are going to need certain data - you will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a certain price, which is given bellow:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If a price for a certain item is higher than the maximum price, don’t buy it. Every time you buy an item,
# you have to reduce the budget with the value of its price. If you don’t have enough money for it, you can’t buy it. Buy as much items as you can.
# You have to increase the price of each of the items you have successfully bought with 40%.
# Print the list with the new prices and the profit you will gain from selling the items.
# They need exactly 150$ for tickets for the train, so if their budget after selling the products is enough – print – "Hello, France!" and if not – "Time to go."

items = input().split('|')
budget = float(input())

old_prices = []
new_prices = []

for item_index in range(len(items)):
    current_item = items[item_index].split('->')
    current_item_type = current_item[0]
    current_item_price = float(current_item[1])

    if budget < current_item_price:
        continue

    if current_item_type == 'Clothes' and current_item_price > 50:
        continue
    if current_item_type == 'Shoes' and current_item_price > 35:
        continue
    if current_item_type == 'Accessories' and current_item_price > 20.50:
        continue

    budget -= current_item_price
    current_item_price_new = 1.4 * current_item_price
    old_prices.append(current_item_price)
    new_prices.append(current_item_price_new)

budget += sum(new_prices)
profit = sum(new_prices) - sum(old_prices)

for new_price in new_prices:
    print(f'{new_price:.2f}', end = ' ')

print()
print(f'Profit: {profit:.2f}')

if budget > 150:
    print('Hello, France!')
else:
    print('Time to go.')