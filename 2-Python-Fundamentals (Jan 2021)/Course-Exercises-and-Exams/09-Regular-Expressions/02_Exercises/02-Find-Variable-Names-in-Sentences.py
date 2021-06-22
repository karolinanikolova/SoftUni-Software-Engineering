# 2.	Find Variable Names in Sentences
# Write a program that finds all variable names in a given string. A variable name starts with an underscore ("_")
# and contains only Capital and Non-Capital English Alphabet letters and digits. Extract only their names, without the underscore.
# to do this only with regular expressions.
# The output consists of all variable names, extracted and printed on a single line, each separated by a comma.

import re

text = input()

pattern = r"((?<=\b_)|(?<=\s_))[A-Za-z0-9]+\b"

matches = [matched_obj.group() for matched_obj in re.finditer(pattern, text)]

print(",".join(matches))

