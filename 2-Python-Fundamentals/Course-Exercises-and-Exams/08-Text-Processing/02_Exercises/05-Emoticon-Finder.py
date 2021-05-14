# 5.	 Emoticon Finder
# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

# text = input()
#
# for index in range(len(text)):
#     if text[index] == ":" and not index == len(text)-1:
#         print(text[index:index+2])

text = input()

emojis = [f"{text[index]}{text[index + 1]}" for index in range(len(text)) if text[index] == ":"]

print("\n".join(emojis))


