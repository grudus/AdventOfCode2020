import itertools
from collections import defaultdict
from functools import reduce

def first_star(tiles_input):
    tiles = [(tile_line.split("\n")[0], find_borders(tile_line.split("\n")[1:])) for tile_line in tiles_input]
    
    border_count = defaultdict(int)

    for _, borders in tiles:
        for border in borders: border_count[border] += 1
    
    corner_tiles = [int(tile_id[5:-1]) 
        for tile_id, borders in tiles 
        if len([1 for border in borders if border_count[border] == 1]) == 4]
    
    return reduce(int.__mul__, corner_tiles)


def find_borders(tile_lines):
    to_binary = lambda line: int("".join(["1" if tile == '#' else "0" for tile in line]), 2)

    top = tile_lines[0]
    bottom = tile_lines[-1]
    left = [line[0] for line in tile_lines]
    right = [line[-1] for line in tile_lines]

    return [to_binary(top), to_binary(top[::-1]),
        to_binary(right), to_binary(right[::-1]),
        to_binary(bottom), to_binary(bottom[::-1]), 
        to_binary(left), to_binary(left[::-1])]



if __name__ == "__main__":
    tiles_input = open('src/main/resources/day20/input.txt', 'r').read().split("\n\n")
    print(first_star(tiles_input))