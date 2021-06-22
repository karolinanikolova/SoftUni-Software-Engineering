# perimeter and face of a circle
# Write a program that reads the number r from the console and calculates and prints the area and perimeter of a circle / circle of radius r .

from math import pi

r = float(input())

area = pi * r * r
perimeter = 2 * pi * r

print(f'Area ={area}')
print(f'Perimeter ={perimeter}')
