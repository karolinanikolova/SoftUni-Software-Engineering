# 2.	Calculations
# Create a function that receives three parameters and calculates a result depending on operator.
# The operator can be  'multiply', 'divide', 'add', 'subtract' . The input comes as three parameters –
# two integers and an operator as a string.

def calculate(operator, num1, num2):
    if operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        result = num1 // num2
    elif operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    return result

action = input()
first_number = int(input())
second_number = int(input())

res = calculate(action, first_number, second_number)
print(res)

