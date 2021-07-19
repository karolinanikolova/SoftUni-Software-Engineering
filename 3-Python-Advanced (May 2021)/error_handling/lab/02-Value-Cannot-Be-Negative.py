# 2.	Value Cannot Be Negative
# Create your own exception called ValueCannotBeNegative.
# Write a program that reads five numbers from the console (on separate lines).
# If a negative number occurs, raise the exception.

from error_handling.lab.errors import ValueCannotBeNegative

for _ in range(5):
    number = float(input())
    if number < 0:
        raise ValueCannotBeNegative

