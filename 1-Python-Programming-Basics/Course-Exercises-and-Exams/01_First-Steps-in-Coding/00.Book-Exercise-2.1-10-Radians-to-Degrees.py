# cantilever converter - from radians to degrees
# Write a program that reads the angle in radians ( rad) and converts it into degrees ) ( deg).
# Search the Internet for a suitable formula. The number π in Python programs is accessible via math.pi and we must first refer to the math library via import math.
# Round the result to the nearest whole number using the method round().

from math import pi

rad = float(input())
deg = round(rad * 180 / pi)
print(deg)

