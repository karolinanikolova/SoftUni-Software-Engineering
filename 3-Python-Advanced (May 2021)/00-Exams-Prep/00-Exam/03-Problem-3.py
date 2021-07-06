# Problem 3
# Write a function named math_operations that receives different number of integers as arguments and 4 keyword arguments.
# The keys will be single letters: "a", "s", "d", "m" and the values will be numbers.
# You need to take each integer argument from the sequence and do mathematical operation as follows:
# •	The first element should be added to the value of the key "a"
# •	The second element should be subtracted from the value of the key "s"
# •	The third element should be divisor to the value of the key "d"
# •	The fourth element should be multiplied by the value of the key "m"
# •	Each result should replace the value of the corresponding key
# •	You must repeat the same steps consecutively until you run out of numbers
# Beware: You cannot divide by 0. If the operation could throw an error you have to delete the element
# from the sequence and continue to the next operation.
# For more clarifications, see the examples below.
# Note: Submit only the function in the judge system

def math_operations(*args, a, s, d, m):

    my_dict = {'a': a, 's': s, 'd': d, 'm': m}
    args = list(args)

    current_element_count = 1

    while args:

        if current_element_count % 4 == 1:
            my_dict['a'] += args[0]
            args.pop(0)
        elif current_element_count % 4 == 2:
            my_dict['s'] -= args[0]
            args.pop(0)
        elif current_element_count % 4 == 3:
            divisor = args[0]
            if divisor == 0:
                args.pop(0)
            else:
                my_dict['d'] /= args[0]
                args.pop(0)
        else:
            my_dict['m'] *= args[0]
            args.pop(0)

        current_element_count += 1

    return my_dict


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))


