import math

def first_star(navigation_actions):
    navigation_actions = [(action[0], int(action[1:]))  for action in navigation_actions]
    position = (0, 0)
    direction = (1, 0)

    for action, value in navigation_actions:
        if action == 'F':
            position = (position[0] + value * direction[0], position[1] + value * direction[1])
        elif action == 'N':
            position = (position[0], position[1] + value)
        elif action == 'E':
            position = (position[0] + value, position[1])
        elif action == 'S':
            position = (position[0], position[1] - value)
        elif action == 'W':
            position = (position[0] - value, position[1])
        elif action == 'R':
            direction = rotate(direction, value)
        elif action == 'L':
            direction = rotate(direction, -value)
    
    return abs(position[0]) + abs(position[1])
            

def second_star(navigation_actions):
    navigation_actions = [(action[0], int(action[1:]))  for action in navigation_actions]
    ship_position = (0, 0)
    waypoint_position = (10, 1)

    for action, value in navigation_actions:
        if action == 'F':
            ship_position = (ship_position[0] + value * waypoint_position[0], ship_position[1] + value * waypoint_position[1])
        elif action == 'N':
            waypoint_position = (waypoint_position[0], waypoint_position[1] + value)
        elif action == 'E':
            waypoint_position = (waypoint_position[0] + value, waypoint_position[1])
        elif action == 'S':
            waypoint_position = (waypoint_position[0], waypoint_position[1] - value)
        elif action == 'W':
            waypoint_position = (waypoint_position[0] - value, waypoint_position[1])
        elif action == 'R':
            waypoint_position = rotate(waypoint_position, value)
        elif action == 'L':
            waypoint_position = rotate(waypoint_position, -value)

    return abs(ship_position[0]) + abs(ship_position[1])
            

def rotate(point, angle):
    angle = -math.radians(angle)
    ox, oy = (0, 0)
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))
        

if __name__ == "__main__":
    navigation_actions = open('src/main/resources/day12/input.txt', 'r').read().split("\n")
    print(first_star(navigation_actions))
    print(second_star(navigation_actions))