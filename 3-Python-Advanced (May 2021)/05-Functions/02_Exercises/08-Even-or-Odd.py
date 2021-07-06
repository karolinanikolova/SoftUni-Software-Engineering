# 8.	Even or Odd
# Create a function called even_odd() that can receive different amount of numbers and a command at the end.
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.

def even_odd(*args):
    com = args[-1]
    if com == "odd":
        return list(filter(lambda x: x % 2 != 0, args[0:-1]))
    return list(filter(lambda x: x % 2 == 0, args[0:-1]))

# Test code
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))