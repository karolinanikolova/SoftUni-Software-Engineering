# 1.	Biggest of Three Numbers
# Write a program that receives three whole numbers and print the biggest one

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

# print(max(a, b, c))
