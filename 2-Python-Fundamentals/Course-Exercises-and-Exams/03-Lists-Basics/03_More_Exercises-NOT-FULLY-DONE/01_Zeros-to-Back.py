# 1.	Zeros to Back
# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros and moves them to the back without messing up the other elements. Print the resulting integer list

string = input().split(', ')

numbers = list(map(int, string))

for element in range(len(numbers)-1, -1, -1):
    numbers.remove(0)
    numbers.append(0)

print(numbers)