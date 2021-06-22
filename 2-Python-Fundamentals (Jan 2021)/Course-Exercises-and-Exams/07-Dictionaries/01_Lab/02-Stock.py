# 2.	Stock
# After you have successfully completed your first task, your boss decides to give you another one right away.
# Now not only you have to keep track of the stock, but also you have to answer customers if you have some products in stock or not.
# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the next line you will be given products to search for. Check for each product, you have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left"
# •	Otherwise, print "Sorry, we don't have {product}"

data = input().split()
products = {}
searched_products = input().split()

for index in range(0, len(data), 2):
    current_stock = data[index]
    stock_value = int(data[index + 1])
    products[current_stock] = stock_value

for s_product in searched_products:
    if s_product not in products:
        print(f"Sorry, we don't have {s_product}")
    else:
        print(f"We have {products[s_product]} of {s_product} left")


