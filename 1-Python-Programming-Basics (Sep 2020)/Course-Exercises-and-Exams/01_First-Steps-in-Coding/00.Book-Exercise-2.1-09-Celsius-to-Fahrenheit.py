# cantilever converter - from degrees ° C to degrees ° F
# Write a program that reads degrees on the Celsius scale (° C) and converts them to degrees on the Fahrenheit scale (° F).
# Search the Internet for a suitable formula to perform the calculations. Round the result to 2 characters after the decimal point .

celsius = float(input())
fahrenheit = round(((celsius * 9 / 5) + 32), 2)
print(fahrenheit)