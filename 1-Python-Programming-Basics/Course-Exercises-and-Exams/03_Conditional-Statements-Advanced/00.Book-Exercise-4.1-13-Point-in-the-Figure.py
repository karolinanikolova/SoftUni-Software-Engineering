# точка във фигурата
# Фигура се състои от 6 блокчета с размер h * h, разположени като на фигурата. Долният ляв ъгъл на сградата е на позиция {0, 0}.
# Горният десен ъгъл на фигурата е на позиция {2*h, 4*h}. На фигурата координатите са дадени при h = 2:
#
# Да се напише програма, която въвежда цяло число h и координатите на дадена точка {x, y} (цели числа) и отпечатва дали
# точката е вътре във фигурата (inside), вън от фигурата (outside) или на някоя от стените на фигурата (border).

h = int(input())
x = float(input())
y = float(input())

# check to see if dot is inside rectangle 1
dot_inside_horizontal_rectangle = 0 < x < (3 * h) and 0 < y < h
# check to see if dot is inside rectangle 2
dot_inside_vertical_rectangle = h < x < (2 * h) and 0 < y < (4 * h)

# check to see if dot is on one of the borders
dot_on_bottom_border = 0 <= x <= (3 * h) and y == 0
dot_on_middle_border = (0 <= x <= h or (2 * h) <= x <= (3 * h)) and y == h
dot_on_top_border = h <= x <= (2 * h) and y == (4 * h)
dot_on_left_border = x == 0 and 0 <= y <= h
dot_on_middle_left_border = x == h and h <= y <= (4 * h)
dot_on_middle_right_border = x == (2 * h) and h <= y <= (4 * h)
dot_on_right_border = x == (3 * h) and 0 <= y <= h

if dot_inside_horizontal_rectangle or dot_inside_vertical_rectangle:
    print('inside')
elif dot_on_bottom_border or dot_on_middle_border or dot_on_top_border or dot_on_left_border or \
         dot_on_middle_left_border or dot_on_middle_right_border or dot_on_right_border:
    print('border')
else:
    print('outside')