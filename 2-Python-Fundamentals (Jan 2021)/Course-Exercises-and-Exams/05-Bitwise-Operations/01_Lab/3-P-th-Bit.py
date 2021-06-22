# 4.	Print the result on the console.
# 3.	P-th Bit
# Write a program that prints the bit at position p of given integer. We use the standard counting: from right to left, starting from 0.

n = int(input())
p = int(input())

print((n >> p) & 1)