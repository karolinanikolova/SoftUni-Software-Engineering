# 2.	File Reader
# You are given a file called numbers.txt with the following content:
# Create a program that reads the numbers from the file. Print on the console the sum of those numbers.

file = open("numbers.txt")

numbers = [int(line) for line in file]

print(sum(numbers))

file.close()

# result = 0
#
# for line in file:
#     result += int(line)
#
# print(result)