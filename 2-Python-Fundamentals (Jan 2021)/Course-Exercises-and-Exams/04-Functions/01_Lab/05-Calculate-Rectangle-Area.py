# 5.	Calculate Rectangle Area
# Create a function that calculates and returns the area of a rectangle by given width and height:

def calculate_rectangle_area(wide, high):
    return wide * high


width = int(input())
height = int(input())

result = calculate_rectangle_area(width, height)
print(result)