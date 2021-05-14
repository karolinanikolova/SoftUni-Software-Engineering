# 4. Orders
# Write a function that calculates the total price of an order and prints it on the console.
# The function should receive one of the following products: coffee, coke, water, snacks;
# and a quantity of the product. The prices for a single piece of each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
# Print the result formatted to the second decimal place.

def order_price(product, product_quantity):
    if product == 'coffee':
        product_price = 1.50
    elif product == 'water':
        product_price = 1
    elif product == 'coke':
        product_price = 1.4
    elif product == 'snacks':
        product_price = 2
    return product_price * product_quantity


product_name = input()
product_count = int(input())

result = order_price(product_name, product_count)
print(f'{result:.2f}')
