# 4.	Number Classification
# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
# and prints all the positive, negative, even and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number


numbers = [int(el) for el in input().split(', ')]

positive = [n for n in numbers if n >= 0]
negative = [n for n in numbers if n < 0]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if not n % 2 == 0]

print(f"Positive: {', '.join([str(el) for el in positive])}")
print(f"Negative: {', '.join([str(el) for el in negative])}")
print(f"Even: {', '.join([str(el) for el in even])}")
print(f"Odd: {', '.join([str(el) for el in odd])}")
