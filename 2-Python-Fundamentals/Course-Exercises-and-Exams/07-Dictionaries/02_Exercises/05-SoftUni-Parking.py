# 5.	SoftUni Parking
# SoftUni just got a new parking lot. It's so fancy, it even has online parking validation. Except the online service doesn't work.
# It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place for an online service. Users can register to park and unregister to leave.
# The program receives 2 types of commands:
# •	"register {username} {licensePlateNumber}":
# o	The system only supports one car per user at the moment, so if a user tries to register another license plate,
# using the same username, the system should print:
# "ERROR: already registered with plate number {licensePlateNumber}"
# o	If the aforementioned checks passes successfully, the plate can be registered, so the system should print:
#  "{username} registered {licensePlateNumber} successfully"
# •	"unregister {username}":
# o	If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
# o	If the aforementioned check passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all of the commands, print all the currently registered users and their license plates in the format:
# •	"{username} => {licensePlateNumber}"

n = int(input())

users = {}

for _ in range(n):
    command = input().split()
    action = command[0]

    if action == "register":
        username = command[1]
        license_plate_number = command[2]
        if username in users:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif action == "unregister":
        username = command[1]
        if username not in users:
            print(f"ERROR: user {username} not found")
        else:
            users.pop(username)
            print(f"{username} unregistered successfully")

for username, license_plate_number in users.items():
    print(f"{username} => {license_plate_number}")