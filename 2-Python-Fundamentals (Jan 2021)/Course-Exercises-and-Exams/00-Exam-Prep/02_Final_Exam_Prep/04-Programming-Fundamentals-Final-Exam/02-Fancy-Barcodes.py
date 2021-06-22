# Problem 2. Fancy Barcodes
# Your first task is to determine if the given sequence of characters is a valid barcode or not.
# Each line must not contain anything else but a valid barcode. A barcode is valid when:
# •	Is surrounded with a "@" followed by one or more "#"
# •	Is at least 6  characters long (without the surrounding "@" or "#")
# •	Starts with a capital letter
# •	Contains only letters (lower and upper case) and digits
# •	Ends with a capital letter
# Examples of valid barcodes: @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##, @##Che46sE@###
# Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#
# Next you have to determine the product group of the item from the barcode. The product group is obtained by concatenating
# all the digits found in the barcode. If there are no digits present in the barcode, the default product group is "00".
# Examples:
# @#FreshFisH@# -> product group: 00
# @###Brea0D@### -> product group: 0
# @##Che4s6E@## -> product group: 46

import re

n = int(input())

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
pattern_digits = r"\d"

for _ in range(n):
    barcode = input()
    valid_barcode = "".join(re.findall(pattern, barcode))
    if valid_barcode:
        product_group = "".join(re.findall(pattern_digits, valid_barcode))
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
