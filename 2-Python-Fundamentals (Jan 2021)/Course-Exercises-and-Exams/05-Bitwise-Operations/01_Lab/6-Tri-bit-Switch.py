# 6.	* Tri-bit Switch
# Write a program that inverts the 3 bits from position p to the left with their
#     XOR opposites (e.g. 111 -> 000, 101 -> 010) in 32-bit number. Print the resulting integer on the console.

number = int(input())
p = int(input())

mask = 7 << p

result = number ^ mask

print(result)