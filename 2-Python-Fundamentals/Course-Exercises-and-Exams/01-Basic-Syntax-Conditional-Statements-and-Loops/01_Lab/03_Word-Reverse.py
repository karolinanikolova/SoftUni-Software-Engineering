# 3.	Word Reverse
# Write a program that receives a single word from the user, reverses it and prints it

word = input()

reversed_word = ''

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print(reversed_word)

# print(word[::-1]) # collection with cells (e.g. the word HELLO in cells and each cell has a number assigned starting from 0.
# # The syntax in the brackets is showing the slicing of this collection. :: means from the beginning to the end.


