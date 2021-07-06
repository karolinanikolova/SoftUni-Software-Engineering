# 9.	Function Executor
# Create a function called func_executor() that can receive different number of tuples, each of which will have
# exactly 2 elements: first will be a function and the second will be a tuple of the arguments that need to be passed
# to that function. Create a list which will contain all the results of the executed functions with its corresponding
# arguments. For more clarification, see the examples below. Submit only your function in the judge system.

def func_executor(*args):
    result = []
    for func_name, data in args:
        result.append(func_name(*data))
    return result

# Test code
def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
