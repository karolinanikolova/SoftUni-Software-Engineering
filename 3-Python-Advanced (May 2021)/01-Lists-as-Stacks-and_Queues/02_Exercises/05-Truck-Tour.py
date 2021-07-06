# 5. Truck Tour
# On a circle road there are N petrol pumps. Petrol pumps are numbered 0 to (N−1) (both inclusive).
# For each petrol pump you will receive two pieces of information:
# -	the amount of petrol that petrol pump will give
# -	the distance from that petrol pump to the next petrol pump (kilometers)
# Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps.
# Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop
# at each of the petrol pumps. The truck will move one kilometer for each liter of the petrol.

from collections import deque
N = int(input())

stations = deque()

for _ in range(N):
    stations.append(input())

for big_circle_iteration in range(N):
    is_valid = True
    tank_petrol = 0

    for small_circle_iteration in range(N):
        current_station = stations[small_circle_iteration]
        petrol, distance_to_next_station = current_station.split()
        petrol = int(petrol)
        distance_to_next_station = int(distance_to_next_station)

        tank_petrol += petrol - distance_to_next_station

        if tank_petrol < 0:
            is_valid = False
            stations.append(stations.popleft())
            break

    if is_valid:
        print(big_circle_iteration)
        break