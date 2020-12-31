import itertools
from collections import defaultdict
from functools import reduce
import typing
import dataclasses

Id = int
Area = typing.Text

@dataclasses.dataclass
class Borders:
    top: typing.Tuple[int, int]
    right: typing.Tuple[int, int]
    bottom: typing.Tuple[int, int]
    left: typing.Tuple[int, int]

    def to_set(self):
        return set(self.top) | set(self.right) | set(self.bottom) | set(self.left)


def first_star(tiles_input):
    tiles = parse_tiles_input(tiles_input)
    tile_to_neighbours = find_neighbours(tiles)
    corner_tiles = [tile_id for tile_id, neighbours in tile_to_neighbours.items() if len(neighbours) == 2]
    return reduce(int.__mul__, corner_tiles)


def second_star(tiles_input):
    tiles = parse_tiles_input(tiles_input)
    tile_to_neighbours = find_neighbours(tiles)
    world_map = {}

    for tile_id, neighbours in tile_to_neighbours.items():
        if not world_map and len(neighbours) == 2: # first corner 
            
            area, borders = tiles[tile_id]
            world_map[(0, 0)] = area
            
            print(borders)
            

            for neighbour in neighbours:
                n_area, n_borders = tiles[neighbour]
                print(n_borders)
            
            break

    for coord, area in world_map.items():
        for row in area:
            print(row)
        print()



def find_neighbours(tiles: typing.Dict[Id, typing.Tuple[Area, Borders]]) -> typing.DefaultDict[Id, typing.List[Id]]:
    tile_to_neighbours = defaultdict(list)

    for tile_id, (_, borders) in tiles.items():

        for tile2_id, (_, borders2) in tiles.items():
            common_borders = borders.to_set() & borders2.to_set()
            if common_borders and tile_id != tile2_id: tile_to_neighbours[tile_id].append(tile2_id)

    return tile_to_neighbours


def parse_tiles_input(tiles_input: typing.List[str]) -> typing.Dict[Id, typing.Tuple[Area, Borders]]:
    return {int(tile_id[5:-1]): (area, find_borders(area)) 
        for tile_id, *area in 
            [single_area.split("\n") for single_area in tiles_input]
        }



def find_borders(tile_lines) -> Borders:
    to_binary = lambda line: int("".join(["1" if tile == '#' else "0" for tile in line]), 2)

    top = tile_lines[0]
    bottom = tile_lines[-1]
    left = [line[0] for line in tile_lines]
    right = [line[-1] for line in tile_lines]

    return Borders(
        (to_binary(top), to_binary(top[::-1])),
        (to_binary(right), to_binary(right[::-1])),
        (to_binary(bottom), to_binary(bottom[::-1])), 
        (to_binary(left), to_binary(left[::-1]))
    )


if __name__ == "__main__":
    tiles_input = open('src/main/resources/day20/input.txt', 'r').read().split("\n\n")
    print(first_star(tiles_input))
    print(second_star(tiles_input))