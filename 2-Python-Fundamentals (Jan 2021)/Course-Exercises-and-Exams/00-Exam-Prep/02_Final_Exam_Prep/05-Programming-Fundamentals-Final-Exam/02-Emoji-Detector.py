# Problem 2. Emoji Detector
# Your task is to write program which extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.
# The cool threshold could be a very big number, so be mindful.
# An emoji is valid when:
# •	Is surrounded by either :: or ** (exactly 2)
# •	Is at least 3 characters long (without the surrounding symbols)
# •	Starts with a capital letter
# •	Continues with lowercase letters only
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
# You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is
# determined by summing all the ASCII values of all letters in the emoji.
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of cool threshold and after that to take all emojis out of the text, count them
# and print the only the cool ones on the console.

import re

text = input()
cool_threshold = 1
emojis_coolness = []
cool_emojis = []

pattern_cool_threshold = r"\d"

# pattern_emojis = r"(?<=(::|\*\*))[A-Z][a-z][a-z]+(?=\1)"
pattern_emojis = r"(::|\*\*)[A-Z][a-z][a-z]+(\1)"

cool_threshold_digits = [int(el) for el in re.findall(pattern_cool_threshold, text)]

# cool_threshold = [cool_threshold := cool_threshold * el for el in cool_threshold_digits][-1]

for el in cool_threshold_digits:
    cool_threshold = cool_threshold * el

valid_emojis = [match.group() for match in re.finditer(pattern_emojis, text)]

for emoji in valid_emojis:
    emoji_coolness = 0
    for index in range(len(emoji)):
        if index == 0 or index == 1 or index == len(emoji) - 1 or index == len(emoji) - 2:
            continue
        character = emoji[index]
        emoji_coolness += ord(character)
    emojis_coolness.append(emoji_coolness)

cool_emojis = [valid_emojis[index] for index in range(len(emojis_coolness)) if emojis_coolness[index] > cool_threshold]

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
if cool_emojis:
    print("\n".join(cool_emojis))

