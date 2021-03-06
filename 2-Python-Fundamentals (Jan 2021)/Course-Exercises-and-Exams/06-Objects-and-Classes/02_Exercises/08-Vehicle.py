# 8.	* Vehicle
# Create a class Vehicle. The __init__ method should receive: type, model, price.
# You should also set the owner to None. The class should have the following methods:
# •	buy(money, owner) - if the person has enough money and the vehicle has no owner, returns:
# "Successfully bought a {type}. Change: {change}" and sets the owner to the given one.
# If the money is not enough, return: "Sorry, not enough money". If the car already has an owner, return: "Car already sold"
# •	sell() - if the car has an owner, set it to None again. Otherwise, return: "Vehicle has no owner"
# •	__repr__() - returns "{model} {type} is owned by: {owner}" if the vehicle has an owner.
# Otherwise, return: "{model} {type} is on sale: {price}"

class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        if self.owner:
            return "Car already sold"
        if money >= self.price:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
