# You are given an array with integers. Write a program to modify the elements after receive the commands “swap”, “multiply” or “decrease”.
# •	“swap {index1} {index2}” take two elements and swap their places.
# •	“multiply {index1} {index2}” take element at the 1st index and multiply it with element at 2nd index. Save the product at the 1st index.
# •	“decrease” decreases all elements in the array with 1.

array = [int(el) for el in input().split()]

command_data = input()

while not command_data == "end":
    command_data = command_data.split()
    action = command_data[0]

    if action == "swap":
        index1 = int(command_data[1])
        index2 = int(command_data[2])
        array[index1], array[index2] = array[index2], array[index1]
    elif action == "multiply":
        index1 = int(command_data[1])
        index2 = int(command_data[2])
        array[index1] = array[index1] * array[index2]
    elif action == "decrease":
        array = [el-1 for el in array]

    command_data = input()

array = [str(el) for el in array]

print(", ".join(array))
