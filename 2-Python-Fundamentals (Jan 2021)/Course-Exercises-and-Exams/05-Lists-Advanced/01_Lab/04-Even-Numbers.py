# 4.	Even Numbers
# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers

nums_as_string = input().split(", ")

# even_numbers_indices = [index for index in range(len(numbers_as_string)) if int(numbers_as_string[index]) % 2 == 0]

nums = [int(num) for num in nums_as_string]
# nums_map = list(map(lambda el: int(el), nums_as_string))
# nums_map_ref = list(map(int, nums_as_string))

even_numbers_indices = [index for index in range(len(nums)) if nums[index] % 2 == 0]
# even_numbers_indices_filter = [nums.index(el) for el in list(filter(lambda num: num % 2 == 0, nums))]
# even_numbers_indices_filter = list(map(lambda el: nums.index(el), list(filter(lambda num: num % 2 == 0, nums))))

print(even_numbers_indices)