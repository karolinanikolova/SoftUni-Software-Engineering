# Problem 1. Computer Store
# Write a program that prints you a receipt for your new computer.
# You will receive the prices (without tax) of the parts until you receive what type of customer is this - special or regular.
# Once you receive the type of the customer you should print the receipt.
# The taxes are 20% of each part's price you receive.
# If the customer is special, then he has a 10% discount of the price of the total price with taxes.
# If a given price is not positive number, you should print "Invalid price!" on the console and continue with the next price.
# If total price is equal to zero, you should print "Invalid order!" on the console.

command = input()

price_without_tax = 0

while not command == "special" and not command == "regular":
    part_price_without_tax = float(command)

    if part_price_without_tax <= 0:
        print("Invalid price!")
    else:
        price_without_tax += part_price_without_tax

    command = input()

taxes = 0.2 * price_without_tax
final_price = price_without_tax + taxes

if command == "special":
    final_price = 0.9 * final_price

if final_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")

