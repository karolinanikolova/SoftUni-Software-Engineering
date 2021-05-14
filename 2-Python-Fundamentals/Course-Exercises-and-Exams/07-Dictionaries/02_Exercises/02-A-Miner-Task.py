# 2.	A Miner Task
# You will be given a sequence of strings, each on a new line. Every odd line on the console is representing a resource
# (e.g. Gold, Silver, Copper, and so on) and every even – quantity. Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# {resource} –> {quantity}
# The quantities will be in the range [1 … 2 000 000 000]

command = input()

line_counter = 0
resources = {}

while not command == "stop":
    line_counter += 1
    if line_counter % 2 == 1:
        resource = command
        if resource not in resources:
            resources[resource] = 0
    else:
        quantity = command
        resources[resource] += float(quantity)
    command = input()

for resource, quantity in resources.items():
    print(f"{resource} -> {round(quantity)}")
