# 1.	Integer Operations
# Read four integer numbers. Add first to the second, divide (integer) the sum by the third number and multiply the result by the fourth number. Print the result.

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
number_4 = int(input())

result = int((number_1 + number_2) / number_3) * number_4

print(result)