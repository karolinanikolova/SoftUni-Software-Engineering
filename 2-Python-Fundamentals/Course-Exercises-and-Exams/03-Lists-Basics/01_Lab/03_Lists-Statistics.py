# 3.	List Statistics
# You will be given a number n. On the next n lines you will receive integers. You have to create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"

n = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {len(positive_numbers)}. Sum of negatives: {sum(negative_numbers)}')