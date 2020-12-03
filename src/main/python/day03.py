
def first_star(forest):
    current_coord = (0, 0)
    forest_size_y = len(forest)
    forest_size_x = len(forest[0])
    num_of_trees = 0

    while current_coord[1] < (forest_size_y - 1):
        next_coord = (current_coord[0] + 3, current_coord[1] + 1)

        if next_coord[0] >= forest_size_x:
            next_coord = (next_coord[0] - forest_size_x, next_coord[1])
           
        if forest[next_coord[1]][next_coord[0]] == '#':
            num_of_trees += 1

        current_coord = next_coord

    return num_of_trees




forest = open('src/main/resources/day03/input.txt', 'r').read().split("\n")

print(first_star(forest))
