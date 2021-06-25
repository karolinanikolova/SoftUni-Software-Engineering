# 12.	Recursion Palindrome
# Write a recursive function called palindrome() which will receive a word and an index (always 0).
# Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome"
# if the word is not a palindrome using recursion. Submit only the function in the judge system.

def palindrome(word, index=0):

    if index == len(word) // 2:
        return f"{word} is a palindrome"

    left_char = word[index]
    right_char = word[len(word)-1-index]

    if left_char != right_char:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)


# Test code
print(palindrome("abcba", 0))
print(palindrome("peter", 0))
print(palindrome("aecba", 0))
