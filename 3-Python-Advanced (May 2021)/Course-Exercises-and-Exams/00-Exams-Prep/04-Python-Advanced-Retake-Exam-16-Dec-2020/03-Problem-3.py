# Create a function called get_magic_triangle which will receive a single parameter (integer n) and it should create
# a magic triangle which follows those rules:
# •	We start with this simple triangle [[1], [1, 1]]
# •	We generate the next rows until we reach n amount of rows
# •	Each number in each row is equal to the sum of the two numbers right above it in the triangle
# •	If the current number has no neighbor to the upper left/rigth, we just take the existing neighbor
# After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5

def get_magic_triangle(n, magic_triangle=None):

    if n == 0:
        magic_triangle = [[1]]
    elif n == 1:
        magic_triangle = [[1], [1, 1]]
    else:
        magic_triangle = [[1], [1, 1]]

        for counter in range(1, n-1):
            new_row = [1]
            last_row = magic_triangle[counter]
            for index in range(len(last_row)-1):
                first_el = last_row[index]
                second_el = last_row[index+1]
                sum_el = first_el + second_el
                new_row.append(sum_el)

            new_row.append(1)

            magic_triangle.append(new_row)

    return magic_triangle


# Test code
get_magic_triangle(5)
print(get_magic_triangle(5))