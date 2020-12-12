import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, point): return Point(self.x + point.x, self.y + point.y)
    def __mul__(self, value: int): return Point(self.x * value, self.y * value)
    def __iter__(self): return iter((self.x, self.y))


def first_star(navigation_actions):
    navigation_actions = [(action[0], int(action[1:]))  for action in navigation_actions]
    position = Point(0, 0)
    direction = Point(1, 0)

    for action, value in navigation_actions:
        if action == 'F':
            position = position + direction * value
        elif action == 'N':
            position = position + Point(0, value)
        elif action == 'E':
            position = position + Point(value, 0)
        elif action == 'S':
            position = position + Point(0, -value)
        elif action == 'W':
            position = position + Point(-value, 0)
        elif action == 'R':
            direction = rotate(direction, value)
        elif action == 'L':
            direction = rotate(direction, -value)
    
    return abs(position.x) + abs(position.y)
            

def second_star(navigation_actions):
    navigation_actions = [(action[0], int(action[1:]))  for action in navigation_actions]
    ship_position = Point(0, 0)
    waypoint_position = Point(10, 1)

    for action, value in navigation_actions:
        if action == 'F':
            ship_position = ship_position + waypoint_position * value
        elif action == 'N':
            waypoint_position = waypoint_position + Point(0, value)
        elif action == 'E':
            waypoint_position = waypoint_position + Point(value, 0)
        elif action == 'S':
            waypoint_position = waypoint_position + Point(0, -value)
        elif action == 'W':
            waypoint_position = waypoint_position + Point(-value, 0)
        elif action == 'R':
            waypoint_position = rotate(waypoint_position, value)
        elif action == 'L':
            waypoint_position = rotate(waypoint_position, -value)

    return abs(ship_position.x) + abs(ship_position.y)
            

def rotate(point, angle):
    angle = -math.radians(angle)
    ox, oy = (0, 0)
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return Point(int(round(qx)), int(round(qy)))
        

if __name__ == "__main__":
    navigation_actions = open('src/main/resources/day12/input.txt', 'r').read().split("\n")
    print(first_star(navigation_actions))
    print(second_star(navigation_actions))