# 4.	Negative vs Positive
# You will receive a sequence of numbers (integers), separated by a single space. Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, replace the negative number with its absolute value and print the following:
# •	On the first line print the sum of the negatives
# •	On the second line print the sum of the positives
# •	On the third line:
# o	If the absolute negative number is bigger than the positive number:
# 	"The negatives are stronger than the positives"
# o	If the positive number is bigger than the absolute negative number:
# 	"The positives are stronger than the negatives"

def print_stronger(nums):
    neg_sum = sum(filter(lambda x: x < 0, nums))
    pos_sum = sum(filter(lambda x: x >= 0, nums))
    print(neg_sum, pos_sum, sep='\n')
    if abs(neg_sum) > pos_sum:
        return print("The negatives are stronger than the positives")
    return print("The positives are stronger than the negatives")


nums = list(map(int, input().split()))

print_stronger(nums)
