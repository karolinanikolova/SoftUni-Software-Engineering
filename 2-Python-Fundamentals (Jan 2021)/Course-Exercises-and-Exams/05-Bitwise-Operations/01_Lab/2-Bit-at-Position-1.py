# 2.	Bit at Position 1
# Write a program that prints the bit at position 1 of given integer.
# We use the standard counting: from right to left, starting from 0.

n = int(input())

bit_at_position = 1

print((n >> bit_at_position) & 1)