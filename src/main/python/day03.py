
from operator import mul
from functools import reduce

def first_star(forest):
    return traverse_tree(forest, 3, 1)


def second_star(forest):
    velocities = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [traverse_tree(forest, dx, dy) for (dx, dy) in velocities]
    return reduce(mul, trees)


def traverse_tree(forest, dx, dy):
    current_coord = (0, 0)
    forest_size_y = len(forest)
    forest_size_x = len(forest[0])
    num_of_trees = 0

    while current_coord[1] < (forest_size_y - dy):
        next_coord = (current_coord[0] + dx, current_coord[1] + dy)

        if next_coord[0] >= forest_size_x:
            next_coord = (next_coord[0] - forest_size_x, next_coord[1])
           
        if forest[next_coord[1]][next_coord[0]] == '#':
            num_of_trees += 1

        current_coord = next_coord

    return num_of_trees




forest = open('src/main/resources/day03/input.txt', 'r').read().split("\n")

print(first_star(forest))
print(second_star(forest))
