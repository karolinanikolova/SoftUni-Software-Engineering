import re

n = int(input())

pattern = r"U\$(?P<username>[A-Z][a-z]{2,})U\$P@\$(?P<password>[A-Za-z]{5,}[0-9]+)P@\$"

count_successful_registrations = 0

for _ in range(n):
    registration = input()
    username = ""
    password = ""

    # valid_registration = [match.group() for match in re.finditer(pattern, registration)]
    for match in re.finditer(pattern, registration):
        username = match.group("username")
        password = match.group("password")

    if username and password:
        print("Registration was successful")
        print(f"Username: {username}, Password: {password}")
        count_successful_registrations += 1
    else:
        print("Invalid username or password")

print(f"Successful registrations: {count_successful_registrations}")

