# 2.	Exchange Integers
# Read two integer numbers and after that exchange their values by using some programming logic. Print the variable values
# before and after the exchange, as shown below:

a = int(input())
b = int(input())

print('Before:')
print(f'a = {a}')
print(f'b = {b}')

c = a
d = b

a = d
b = c

print('After:')
print(f'a = {a}')
print(f'b = {b}')
