# face of a triangle
# Write a program that reads from the console the side and height of a triangle and calculates its face.
# Use the formula for the face of a triangle: area = a * h / 2 . Round the result to 2 digits after the decimal point using the function round(area, 2)

a = float(input())
h = float(input())
area = a * h / 2
result = round(area, 2)

print (f'Triangle area ={result}')

