from lab.math_operations.operations import add, divide, multiply, power, subtract


def calculate_expression(expression):
    (x, sign, y) = expression.split(' ')
    x = float(x)
    y = float(y)
    result = None
    if sign == '+':
        result = add(x, y)
    elif sign == '/':
        result = divide(x, y)
    elif sign == '*':
        result = multiply(x, y)
    elif sign == '^':
        result = power(x, y)
    elif sign == '-':
        result = subtract(x, y)
    else:
        raise Exception(f'Invalid sign {sign}')
    return result

