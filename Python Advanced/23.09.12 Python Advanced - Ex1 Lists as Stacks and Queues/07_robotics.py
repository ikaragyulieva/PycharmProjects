# There is a robotics factory. The current project is assembly-line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product.
# When a robot is free, it should take a product for processing and log its name, product, and processing start time.
# Each robot processes a product coming from the assembly line.
# A product is coming from the line each second (so the first product should appear at [start time + 1 second]).
# If a product passes the line and there is not a free robot to take it,
# it should be queued at the end of the line again.
# The robots are standing in line in the order of their appearance.
# Input
# •	On the first line, you will receive the robots'
# names and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
# •	On the second line, you will get the starting time in the format "hh:mm:ss"
# •	Next, until the "End" command, you will get a product on each line.
# Output
# •	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"

from collections import deque

products = deque()
robots = []
robots_data = input().split(';')
hours, minutes, seconds = [int(x) for x in input().split(':')]
start_time_seconds = hours * 3600 + minutes * 60 + seconds

for robot in robots_data:
    robot_name, processing_time = robot.split('-')
    busy_until_time = 0
    robots.append({'name': robot_name, 'data': [int(processing_time), busy_until_time]})

while True:
    product = input()
    if product == 'End':
        break

    products.append(product)

while products:
    start_time_seconds += 1
    current_product = products.popleft()
    is_taken = False

    for robot in robots:
        if robot['data'][1] <= start_time_seconds:
            robot['data'][1] = start_time_seconds + robot['data'][0]
            h = start_time_seconds // 3600
            m = (start_time_seconds % 3600) // 60
            s = ((start_time_seconds % 3600) % 60)
            h %= 24
            print(f"{robot['name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            is_taken = True
            break

    if not is_taken:
        products.append(current_product)
