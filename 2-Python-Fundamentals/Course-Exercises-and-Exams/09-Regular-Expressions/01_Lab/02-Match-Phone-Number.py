# 2.	Match Phone Number
# Write a regular expression to match a valid phone number from Sofia. After you find all valid phones,
# print them on the console, separated by a comma and a space ", ".
# Compose the Regular Expression
# A valid number has the following characteristics:
# •	It starts with "+359"
# •	Then, it is followed by the area code (always 2)
# •	After that, it's followed by the number itself:
# o	The number consists of 7 digits (separated in two groups of 3 and 4 digits respectively).
# •	The different parts are separated by either a space or a hyphen ('-').

import re

pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"

text = input()

matches = [obj.group() for obj in re.finditer(pattern, text)]

print(", ".join(matches))

