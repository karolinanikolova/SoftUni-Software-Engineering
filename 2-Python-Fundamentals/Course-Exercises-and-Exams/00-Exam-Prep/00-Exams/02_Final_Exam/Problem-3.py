capacity = int(input())

users_dict = {}

command = input()

while not command == "Statistics":
    command = command.split("=")
    action = command[0]

    if action == "Add":
        username = command[1]
        sent_messages = int(command[2])
        received_messages = int(command[3])

        if username not in users_dict:
            users_dict[username] = {"sent": sent_messages, "received": received_messages}

    elif action == "Message":
        sender = command[1]
        receiver = command[2]

        if sender in users_dict and receiver in users_dict:
            users_dict[sender]["sent"] += 1
            users_dict[receiver]["received"] += 1

            if users_dict[sender]["sent"] + users_dict[sender]["received"] == capacity:
                del users_dict[sender]
                print(f"{sender} reached the capacity!")

            if users_dict[receiver]["sent"] + users_dict[receiver]["received"] == capacity:
                del users_dict[receiver]
                print(f"{receiver} reached the capacity!")

    elif action == "Empty":
        username = command[1]

        if username == "All":
            users_dict.clear()

        if username in users_dict:
            del users_dict[username]

    command = input()

sorted_users = sorted(users_dict.items(), key=lambda kvp: (-kvp[1]["received"], kvp[0]))

print(f"Users count: {len(users_dict)}")

for user, user_data in sorted_users:
    sent_messages = user_data["sent"]
    received_messages = user_data["received"]
    count_messages = sent_messages + received_messages

    print(f"{user} - {count_messages}")
