import os

current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)
print(__file__)

# TODO: commented out part to be fixed
path = os.path.abspath(os.path.join(current_dir, "..", "exercises", "demo_test.txt"))

print(path)

with open(path, 'w') as f:
    f.write("Test")

print(os.listdir("./"))
print(os.listdir("../"))
