# 1.	Valid Usernames
# Write a program that reads user names on a single line (joined by ", ") and prints all valid usernames.
# A valid username is:
# •	Has length between 3 and 16 characters
# •	Contains only letters, numbers, hyphens and underscores
# •	Has no redundant symbols before, after or in between

usernames = input().split(", ")

valid_usernames = []
is_valid = True

for username in usernames:
    filtered_username = ''.join(filter(lambda x: x.isalnum() or x == "-" or x == "_", username))
    if 3 < len(username) < 16 and username == filtered_username and username == username.strip():
        valid_usernames.append(username)

print("\n".join(valid_usernames))
