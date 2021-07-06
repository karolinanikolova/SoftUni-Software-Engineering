# 7.	Concatenate
# Write a function called concatenate() that receives some strings, concatenates them, and returns the result.

def concatenate(*args):
    result = ""
    for el in args:
        result += el

    return result


# Test code
print(concatenate("Soft", "Uni", "Is", "Great", "!"))