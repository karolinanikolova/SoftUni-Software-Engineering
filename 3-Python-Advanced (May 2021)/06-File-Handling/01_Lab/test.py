import re

with open("test_file1.txt") as file:
    emails_1 = [line.rstrip() for line in file]
#     or
#     emails_1 = file.read().split()

with open("test_file2.txt") as file:
    emails_2 = [line.rstrip() for line in file]

print(emails_1)
print(emails_2)

overlapping_emails = list(set(emails_1) & set(emails_2))

print(overlapping_emails)