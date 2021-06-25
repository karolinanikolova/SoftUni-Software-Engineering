# 3.	Min Max and Sum
# Write a program that receives a sequence of numbers (integers), separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"

nums = [int(el) for el in input().split()]

print(f"The minimum number is {min(nums)}")
print(f"The maximum number is {max(nums)}")
print(f"The sum number is: {sum(nums)}")
