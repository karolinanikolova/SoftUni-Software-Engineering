# combining text and numbers
# Write a program that reads the console name, surname, age and city and press release of the following type: You are <firstName> <lastName>, a <age>-years old person from <town>.

first_name = input()
last_name = input()
age = int(input())
town = input()

print(f'You are {first_name} {last_name}, a {age}-years old person from {town}.')