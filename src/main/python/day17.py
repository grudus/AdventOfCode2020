from copy import deepcopy
from collections import defaultdict

class Point:
    def __init__(self, x, y, z, w = None):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    def __eq__(self, other): return (self.x, self.y, self.z, self.w) == (other.x, other.y, other.z, other.w)
    def __hash__(self): return hash((self.x, self.y, self.z, self.w))


def first_star(input_lines):
    world = {Point(i,j,0): state for i, line in enumerate(input_lines) for j, state in enumerate(list(line))}
    return number_of_active_cubes_after_cycles(deepcopy(world))
    
def second_star(input_lines):
    world = {Point(i,j,0,0): state for i, line in enumerate(input_lines) for j, state in enumerate(list(line))}
    return number_of_active_cubes_after_cycles(deepcopy(world))


def number_of_active_cubes_after_cycles(world):
    for _ in range(6): world = play_game(world)
    return sum([1 for state in world.values() if state == '#'])


def play_game(world):
    brave_new_world = deepcopy(world)

    for point in world.keys():
        neighbors = find_neighbors(point)
        for neighbor in neighbors: 
            if neighbor not in brave_new_world: brave_new_world[neighbor] = '.'

    for point, state in brave_new_world.items():
        neighbors = find_neighbors(point)
        neighbors_active = len(list(filter(lambda n: n in world and world[n] == '#', neighbors)))

        if state == '#': brave_new_world[point] = '#' if neighbors_active in [2, 3] else '.'
        elif state == '.': brave_new_world[point] = '#' if neighbors_active == 3 else '.'

    return brave_new_world


def find_neighbors(point):
    w_range = [None] if point.w == None else range(point.w - 1, point.w + 2)
    return [Point(x,y,z,w) 
    for x in range(point.x -1, point.x + 2)
    for y in range(point.y - 1, point.y + 2)
    for z in range(point.z - 1, point.z + 2)
    for w in w_range
    if (x, y, z, w) != (point.x, point.y, point.z, point.w)
    ]

if __name__ == "__main__":
    input_lines = open('src/main/resources/day17/input.txt', 'r').read().split("\n")
    print(first_star(input_lines))
    print(second_star(input_lines))