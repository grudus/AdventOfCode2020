import re
from collections import defaultdict
import functools
import operator

class HexGrid:
    def __init__(self):
        self.grid = defaultdict(bool)
        self.directions = {"e": (-1, 1, 0), "se": (-1, 0, 1), "sw": (0, -1, 1), "w": (1, -1, 0), "nw": (1, 0, -1), "ne": (0, 1, -1)}
    
    def instructions_to_coordinate(self, instructions):
        directions = [self.directions[instruction] for instruction in instructions]
        return tuple([sum(direction) for direction in zip(*directions)])
    
    def flip_grid(self, coordinate): self.grid[coordinate] = not self.grid[coordinate]
    def black_tiles_count(self): return sum(self.grid.values())
    def all_coordinates(self): return self.grid.keys()
    def is_black(self, coordinate): return coordinate in self.grid and self.grid[coordinate]

    def find_neighbours(self, coordinate):
        neighbour_coordinates = self.directions.values()
        return [tuple([sum(direction) for direction in zip(coordinate, neighbour_coord)]) for neighbour_coord in neighbour_coordinates]
    
    def expand_border_neighbours(self):
        all_coords = self.grid.keys()
        all_neighbours = [self.find_neighbours(coord) for coord in all_coords]
        expanded = set(functools.reduce(operator.iconcat, all_neighbours, []))
        for coord in expanded:
            if coord not in self.grid: self.grid[coord] = False



def first_star(tile_instructions):
    grid = HexGrid()
    for instruction in tile_instructions: grid.flip_grid(grid.instructions_to_coordinate(instruction))
    return grid.black_tiles_count()

def second_star(tile_instructions):
    grid = HexGrid()
    for instruction in tile_instructions: grid.flip_grid(grid.instructions_to_coordinate(instruction))

    for _ in range(100):
        grid.expand_border_neighbours()
        coords_to_flip = set()

        for coordinate in grid.all_coordinates():
            black_neighbours = sum([grid.is_black(coord) for coord in grid.find_neighbours(coordinate)])

            if (grid.is_black(coordinate) and black_neighbours not in [1,2]) or (not grid.is_black(coordinate) and black_neighbours == 2):
                coords_to_flip.add(coordinate)


        for coord in coords_to_flip: grid.flip_grid(coord)

    return grid.black_tiles_count()


if __name__ == "__main__":
    tile_instructions = list(open('src/main/resources/day24/input.txt', 'r').read().split("\n"))
    tile_instructions = [re.findall(r"(se|sw|nw|ne|e|w)", instruction) for instruction in tile_instructions]
    print(first_star(tile_instructions))
    print(second_star(tile_instructions))
