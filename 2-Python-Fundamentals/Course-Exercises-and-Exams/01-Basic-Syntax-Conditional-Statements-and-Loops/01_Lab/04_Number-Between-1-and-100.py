# 4.	Number Between 1 and 100
# Write a program which reads numbers from the console until it receives a number between 1 and 100 inclusive.
# When the correct number is received, stop reading and print "The number {number} is between 1 and 100"

number = float(input())

# while True:
#     if 1 <= number <= 100:
#         print(f'The number {number} is between 1 and 100')
#         break
#     number = float(input())

while not (1 <= number <= 100):
    number = float(input())

print(f'The number {number} is between 1 and 100')


