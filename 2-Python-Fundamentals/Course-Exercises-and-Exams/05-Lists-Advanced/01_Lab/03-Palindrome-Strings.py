# 3.	Palindrome Strings
# Write a program that receives on the first line words separated by a space and a searched palindrome on the second.
# Print all the palindromes on the first line. Print all the occurrences of the searched palindrome in the format: \
#     "Found palindrome {count} times"

words = input().split()
searched_palindrome = input()

palindrome_words = [word for word in words if word == word[::-1]]

searched_palindrome_counter = palindrome_words.count(searched_palindrome)

print(palindrome_words)
print(f"Found palindrome {searched_palindrome_counter} times")

