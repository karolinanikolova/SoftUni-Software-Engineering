# 7.	*Robotics
# Somewhere in the future, there is a robotics factory. The current project is assembly line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product.
# When a robot is free it should take a product for processing and log his name, product and processing start time.
# Each robot processes a product coming from the assembly line. A product is coming from the line each second
# (so the first product should appear at [start time + 1 second]). If a product passes the line and there is not a
# free robot to take it, it should be queued at the end of the line again.
# The robots are standing on the line in the order of their appearance.

from collections import deque
from datetime import datetime, timedelta

data = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')

robots = []
available_robots = deque()
products = deque()

for el in data:
    robot_data = el.split('-')
    robot = {}
    robot['name'] = robot_data[0]
    robot['processing_time'] = int(robot_data[1])
    robot['available_at'] = time
    robots.append(robot)
    available_robots.append(robot)

product = input()

while not product == 'End':
    products.append(product)
    product = input()

time = time + timedelta(seconds=1)

while products:
    current_product = products.popleft()

    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        robot = [el for el in robots if el == current_robot][0]
        robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= robot['available_at']:
                available_robots.append(r)

        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")

    time = time + timedelta(seconds=1)