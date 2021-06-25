# 1.	Even Numbers
# Write a program that receives a sequence of numbers (integers), separated by a single space.
# It should print a list of only the even numbers. Use filter().

def filter_even(iters):
    return list(filter(lambda x: x % 2 == 0, iters))


nums = map(int, input().split())

print(filter_even(nums))
