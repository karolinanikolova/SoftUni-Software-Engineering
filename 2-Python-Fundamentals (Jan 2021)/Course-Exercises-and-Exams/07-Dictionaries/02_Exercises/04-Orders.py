# 4.	Orders
# Write a program that keeps information about products and their prices. Each product has a name, a price and a quantity.
# If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, which already exists, increase its quantity by the input quantity and if its price is different,
# replace the price as well.
# You will receive products' names, prices and quantities on new lines. Until you receive the command "buy", keep adding items. ' \
#                          'When you do receive the command "buy", print the items with their names and total price of all the products with that name.

# data = input()
#
# products = {}
#
# while not data == "buy":
#     product_name, price, quantity = data.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if product_name not in products:
#         products[product_name] = [price, quantity]
#     else:
#         products[product_name][0] = price
#         products[product_name][1] += quantity
#     data = input()
#
# for product_name, price_and_quantity in products.items():
#     price = float(price_and_quantity[0])
#     quantity = int(price_and_quantity[1])
#     print(f"{product_name} -> {price*quantity:.2f}")

data = input()

products = {}

while not data == "buy":
    product_name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if product_name not in products:
        products[product_name] = {"price": price, "quantity": quantity}
    else:
        products[product_name]["price"] = price
        products[product_name]["quantity"] += quantity

    data = input()

for product_name, price_and_quantity in products.items():
    price = price_and_quantity["price"]
    quantity = price_and_quantity["quantity"]
    print(f"{product_name} -> {price * quantity:.2f}")

# # With two dictionaries
# data = input()
#
# products_prices = {}
# products_quantities = {}
#
# while not data == "buy":
#     product_name, price, quantity = data.split()
#     price = float(price)
#     quantity = int(quantity)
#
#     if product_name not in products_prices:
#         products_prices[product_name] = price
#         products_quantities[product_name] = quantity
#     else:
#         products_prices[product_name] = price
#         products_quantities[product_name] += quantity
#
#     data = input()
#
# for product_name, price in products_prices.items():
#     result = price * products_quantities[product_name]
#     print(f"{product_name} -> {result:.2f}")