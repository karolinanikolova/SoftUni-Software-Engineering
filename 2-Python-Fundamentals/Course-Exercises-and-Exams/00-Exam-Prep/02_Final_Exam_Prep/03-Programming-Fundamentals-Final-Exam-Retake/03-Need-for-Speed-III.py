# Problem 3. Need for Speed III
#
# You have just bought the latest and greatest computer game – Need for Seed III. We know that you can`t wait to start playing.
# Pick your favorite cars and drive them all you want!
# On the first line of the standard input you will receive an integer n – the number of cars that you can obtain.
# On the next n lines the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:
# {car}|{mileage}|{fuel}
# Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
# •	Drive : {car} : {distance} : {fuel}
# o	You need to drive the given distance and you will need the given fuel to do that. If the car doesn`t have enough fuel print:
# "Not enough fuel to make that ride"
# o	If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel with the given fuel and print:
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
# o	You like driving new cars only, so if the mileage of a car reaches 100 000 km, remove it from the collection(s). Print:
# "Time to sell the {car}!"
# •	Refuel : {car} : {fuel}
# o	Refill the tank of your car.
# o	Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank,
# take only what is required to fill it up.
# o	Print a message in the following format:
# "{car} refueled with {fuel} liters"
# •	Revert : {car} : {kilometers}
# o	Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with
# in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
# o	If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
# DO NOT print anything.
# Upon receiving the "Stop" command you need to print all cars in your possession, sorted by their mileage in decscending
# order, then by their name in ascending order, in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."

n = int(input())

cars = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)

    cars[car] = {"mileage": mileage, "fuel": fuel}

command = input()

while not command == "Stop":
    command = command.split(" : ")
    action = command[0]

    if action == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel_needed = int(command[3])

        if fuel_needed > cars[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel_needed
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")

        if cars[car]["mileage"] >= 100000:
            cars.pop(car)
            print(f"Time to sell the {car}!")

    elif action == "Refuel":
        car = command[1]
        fuel_to_be_added = int(command[2])

        if cars[car]["fuel"] + fuel_to_be_added > 75:
            print(f"{car} refueled with {75 - cars[car]['fuel']} liters")
            cars[car]["fuel"] = 75
        else:
            cars[car]["fuel"] += fuel_to_be_added
            print(f"{car} refueled with {fuel_to_be_added} liters")

    elif action == "Revert":
        car = command[1]
        mileage_to_decrease = int(command[2])

        if cars[car]["mileage"] - mileage_to_decrease < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= mileage_to_decrease
            print(f"{car} mileage decreased by {mileage_to_decrease} kilometers")

    command = input()

cars_mileage_descending_name_ascending = dict(sorted(cars.items(), key=lambda kvp: (-kvp[1]["mileage"], kvp[0])))

for car, mileage_and_fuel in cars_mileage_descending_name_ascending.items():
    mileage = mileage_and_fuel["mileage"]
    fuel = mileage_and_fuel["fuel"]

    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
