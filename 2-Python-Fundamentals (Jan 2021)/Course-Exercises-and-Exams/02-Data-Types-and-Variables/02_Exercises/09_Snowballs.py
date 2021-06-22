# 9.	 *Snowballs
# Tony and Andi love playing in the snow and having snowball fights, but they always argue which makes the best snowballs.
# They have decided to involve you in their fray, by making you write a program, which calculates snowball data,
# and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# For each snowball you will receive 3 input lines:
# •	On the first line you will get the snowball_snow – an integer.
# •	On the second line you will get the snowball_time – an integer.
# •	On the third line you will get the snowball_quality – an integer.
# For each snowball you must calculate its snowball_value by the following formula:
# (snowball_snow / snowball_time) ** snowball_quality
# At the end you must print the highest calculated snowball_value.

import sys

number_of_snowballs = int(input())
max_snowball_value = - sys.maxsize

for snowball in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f'{max_snowball_snow} : {max_snowball_time} = {round(max_snowball_value)} ({max_snowball_quality})')
