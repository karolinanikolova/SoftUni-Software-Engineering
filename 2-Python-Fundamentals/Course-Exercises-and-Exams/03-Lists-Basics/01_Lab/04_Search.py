# 4.	Search
# You will receive a number n and a word. On the next n lines you will be given some strings.
# You have to add them in a list and print them.
# After that you have to filter out only the strings that include the given word and print that list too.

n = int(input())
searched_word = input()

all_words = []
matched_words = []

for _ in range(n):
    current_word = input()
    all_words.append(current_word)
    if searched_word in current_word:
        matched_words.append(current_word)

print(all_words)
print(matched_words)

