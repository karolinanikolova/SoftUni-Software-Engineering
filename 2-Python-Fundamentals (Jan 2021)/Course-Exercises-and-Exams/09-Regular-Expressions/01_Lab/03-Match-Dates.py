# 3.	Match Dates
# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy".
# Use capturing groups in your regular expression.
# Compose the Regular Expression
# Every valid date has the following characteristics:
# •	Always starts with two digits, followed by a separator
# •	After that, it has one uppercase and two lowercase letters (e.g. Jan, Mar).
# •	After that, it has a separator and exactly 4 digits (for the year).
# •	The separator could be either of three things: a period ("."), a hyphen ("-") or a forward slash ("/")
# •	The separator needs to be the same for the whole date (e.g. 13.03.2016 is valid, 13.03/2016 is NOT).
# Use a group backreference to check for this.

import re

text = input()

pattern = r"\b(?P<Day>\d{2})(?P<separator>[-./])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})\b"

valid_dates = [match_obj.groupdict() for match_obj in re.finditer(pattern, text)]

print('\n'.join([f"Day: {data['Day']}, Month: {data['Month']}, Year: {data['Year']}" for data in valid_dates]))
