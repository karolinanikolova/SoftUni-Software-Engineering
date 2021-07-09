# 5.	Fibonacci Sequence
# Create a module that can create a Fibonacci sequence up to a number (count of numbers in the sequence) and print them, separating them with a single space. The module should also be able to locate a specific number in the sequence.  You can read more about the Fibonacci sequence here: https://en.wikipedia.org/wiki/Fibonacci_number
# You will be receiving commands until the "Stop" command. The commands are:
# •	"Create Sequence {count}". Create series of numbers up to a specific count and print them in the following format:
#            "{n1} {n2} … {n}"
#
# •	"Locate {number}"
# Check if the sequence contains the number. If, it finds the number it should print:
# "The number - {number} is at index {index}"
# And if it doesn't find it:
# "The number {number} is not in the sequence"

from modules.lab.fibonacci_sequence.fibonacci_sequence import create_sequence, locate


print(*create_sequence(10))
print(locate(13))

print(*create_sequence(3))
print(locate(10))
