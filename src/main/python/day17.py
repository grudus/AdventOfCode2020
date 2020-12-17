from copy import deepcopy
from itertools import product

def first_star(input_lines): return number_of_active_cubes_after_cycles(input_lines, dimension = 3)
def second_star(input_lines): return number_of_active_cubes_after_cycles(input_lines, dimension = 4)


def number_of_active_cubes_after_cycles(input_lines, dimension):
    world = { (x,y) + (0,) * (dimension - 2): state == '#' 
        for x, line in enumerate(input_lines) 
        for y, state in enumerate(list(line)) 
    }
    for _ in range(6): world = play_game(world)
    return list(world.values()).count(True)


def play_game(world):
    brave_new_world = deepcopy(world)

    for point in world.keys():
        neighbors = find_neighbors(point)
        for neighbor in neighbors: 
            if neighbor not in brave_new_world: brave_new_world[neighbor] = False

    for point, is_active in brave_new_world.items():
        neighbors = find_neighbors(point)
        neighbors_active = [world.get(neighbor, False) for neighbor in neighbors].count(True)

        if is_active: brave_new_world[point] = neighbors_active in [2, 3]
        else: brave_new_world[point] = neighbors_active == 3

    return brave_new_world


def find_neighbors(point):
    dimension = len(point)
    offsets = product((-1,0,1), repeat=dimension)
    return [ 
        tuple(dim_point + dim_offset for dim_point, dim_offset in zip(point, offset)) 
        for offset in offsets if offset != (0,) * (dimension)
    ]

if __name__ == "__main__":
    input_lines = open('src/main/resources/day17/input.txt', 'r').read().split("\n")
    print(first_star(input_lines))
    print(second_star(input_lines))