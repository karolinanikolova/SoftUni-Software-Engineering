# 4.	Zoo
# Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals in the zoo.
# The __init__ method should only receive the name of the zoo. There you should also create 3 empty lists (mammals, fishes, birds).
# The class should also have 2 more methods:
# •	add_animal(species, name) - based on the species adds the name to the corresponding list
# •	get_info(species) - based on the species returns a string in the following format:
# "{Species} in {zoo_name}: {names}" and on another line "Total animals: {total_animals}"
# On the first line you will receive the name of the zoo. On the second line you will receive number n.
# On the next n lines you will receive animal info in the format: "{species} {name}".
# Add the animal to the zoo to the corresponding list. The "species" command will be mammal, fish or bird.
# On the final line you will receive a spеcies. At the end, print all the info for that species and the total count of animals.

class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
            Zoo.__animals += 1
        elif species == "fish":
            self.fish.append(name)
            Zoo.__animals += 1
        elif species == "bird":
            self.birds.append(name)
            Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.zoo_name}: {', '.join(self.fish)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
n = int(input())

zoo = Zoo(zoo_name)

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

info = input()

print(zoo.get_info(info))



