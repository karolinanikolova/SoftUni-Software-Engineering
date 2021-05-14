# 2.	Number Definer
# Write a program that reads a floating-point number and prints "zero" if the number is zero.
# Otherwise, print "positive" or "negative". Add "small" if the absolute value of the number is less than 1,
# or "large" if it exceeds 1 000 000.

number = float(input())

if number == 0:
    print('zero')

if number > 0:
    if number > 1000000:
        print('large positive')
    elif number < 1:
        print('small positive')
    else:
        print('positive')

if number < 0:
    if abs(number) > 1000000:
        print('large negative')
    elif abs(number) < 1:
        print('small negative')
    else:
        print('negative')
