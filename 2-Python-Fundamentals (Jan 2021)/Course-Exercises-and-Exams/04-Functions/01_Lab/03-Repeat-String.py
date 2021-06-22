# 3.	Repeat String
# Write a function that receives a string and a repeat count n.
# The function should return a new string (the old one repeated n times).

def repeat_string(string, repeat_times):
    return string * repeat_times


text = input()
n = int(input())

result = repeat_string(text, n)
print(result)
