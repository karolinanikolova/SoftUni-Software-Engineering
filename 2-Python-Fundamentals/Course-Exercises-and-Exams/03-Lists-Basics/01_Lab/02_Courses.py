# 2.	Courses
# You will receive a single number n. On the next n lines you will receive names of courses. You have to create a list of them and print it

n = int(input())

names = []

for _ in range(n):
    name = input()
    names.append(name)

print(names)