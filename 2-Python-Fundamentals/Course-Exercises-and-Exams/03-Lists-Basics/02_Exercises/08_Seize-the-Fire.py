# 8.	* Seize the Fire
# The group of adventurists have gone on their first task. Now they have to walk through fire - literally.
# They have to use all of the water they have left. Your task is to help them survive.
# Create a program that calculates the water that is needed to put out a "fire cell",
# based on the given information about its "fire level" and how much it gets affected by water.
# First, you will be given the level of fire inside the cell with the integer value of the cell,
# which represents the needed water to put out the fire.  They will be given in the following format:
# "{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"
# Afterwards you will receive the amount of water you have for putting out the fires.
# There is a range of fire for each of the fire types, and if a cell’s value is below or exceeds it, it is invalid and you don’t need to put it out.
# Type of Fire	Range
# High	81 - 125
# Medium	51 - 80
# Low	1 - 50
# If a cell is valid, you have to put it out by reducing the water with its value. Putting out fire also takes effort and you need to calculate it. Its value is equal to 25% of the cell’s value. In the end you will have to print the total effort. Keep putting out cells until you run out of water. If you don’t have enough water to put out a given cell – skip it and try the next one. In the end, print the cells you have put out in the following format:
# "Cells:
#  - {cell1}
#  - {cell2}
#  - {cell3}
# ……
#  - {cellN}"
# "Effort: {effort}"
# In the end, print the total fire you have put out from all of the cells in the following format: "Total Fire: {totalFire}"

fires_with_cells = input().split('#')
available_water = int(input())
fires_put_out = []
effort = 0

for fire_index in range(len(fires_with_cells)):

    fire_with_cell = fires_with_cells[fire_index].split(' = ')
    current_fire_type = fire_with_cell[0]
    current_cell_value = int(fire_with_cell[1])

    if current_cell_value > available_water:
        continue

    if current_fire_type == 'High':
        if current_cell_value < 81 or current_cell_value > 125:
            continue

    elif current_fire_type == 'Medium':
        if current_cell_value < 51 or current_cell_value > 80:
            continue

    elif current_fire_type == 'Low':
        if current_cell_value < 1 or current_cell_value > 50:
            continue

    available_water -= current_cell_value
    effort += current_cell_value * .25
    fires_put_out.append(current_cell_value)

print('Cells:')
for fire in fires_put_out:
    print(f'- {fire}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(fires_put_out)}')