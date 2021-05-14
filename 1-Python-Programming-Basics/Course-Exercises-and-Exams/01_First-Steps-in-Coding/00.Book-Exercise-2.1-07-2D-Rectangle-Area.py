# Area and perimeter of a rectangle in the plane
# A rectangle is given by the coordinates of two of its opposite angles (x1, y1) - (x2, y2).
# Calculate its area and perimeter . The input is read from the console. The numbers x1, y1, x2 and y2 are given one per line.
# The output is displayed on the console and must contain two rows with one number on each of them - the area and the perimeter.

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

side_1 = abs(x2 - x1)
side_2 = abs(y2 - y1)

area = side_1 * side_2
perimeter = 2 * (side_1 + side_2)

print(area)
print(perimeter)

