# 3.	Periodic Table
# Write a program that keeps all the unique chemical elements. On the first line you will be given a number n -
# the count of input lines that you are going to receive. On the next n lines, you will be receiving chemical compounds,
# separated by a single space. Your task is to print all the unique ones on separate lines (order does not matter):

n = int(input())

chemical_elements = set()

for _ in range(n):
    additional_chemical_elements = set(input().split())
    chemical_elements = chemical_elements.union(additional_chemical_elements)

[print(chemical_element) for chemical_element in chemical_elements]