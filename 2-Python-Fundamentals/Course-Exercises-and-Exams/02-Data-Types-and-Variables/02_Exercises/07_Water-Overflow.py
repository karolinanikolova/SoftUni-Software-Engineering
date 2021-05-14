# 7.	Water Overflow
# You have a water tank with capacity of 255 liters. On the next n lines, you will receive liters of water,
# which you have to pour in your tank. If the capacity is not enough, print "Insufficient capacity!" and continue reading
# the next line. On the last line, print the liters in the tank.
# Input
# The input will be on two lines:
# •	On the first line, you will receive n – the number of lines, which will follow
# •	On the next n lines – you receive quantities of water, which you have to pour in the tank
# Output
# Every time you do not have enough capacity in the tank to pour the given liters, print:
# Insufficient capacity!
# On the last line, print only the liters in the tank.

n = int(input())

remaining_capacity = 255
liters_added = 0

for _ in range(1, n+1):
    liters_to_add = int(input())
    if remaining_capacity < liters_to_add:
        print('Insufficient capacity!')
    else:
        liters_added += liters_to_add
        remaining_capacity -= liters_to_add

print(liters_added)

