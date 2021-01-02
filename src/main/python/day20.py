import dataclasses
import typing
from collections import defaultdict
from functools import reduce

import numpy as np

Id = int
Area = typing.List[typing.List[chr]]
Coord = typing.Tuple[int, int]


@dataclasses.dataclass
class Borders:
    top: typing.Tuple[int, int]
    right: typing.Tuple[int, int]
    bottom: typing.Tuple[int, int]
    left: typing.Tuple[int, int]

    def to_set(self): return set(self.to_list())

    def to_list(self): return list(self.top) + list(self.right) + list(self.bottom) + list(self.left)


def first_star(tiles_input):
    tiles = parse_tiles_input(tiles_input)
    tile_to_neighbours = find_neighbours(tiles)
    corner_tiles = [tile_id for tile_id, neighbours in tile_to_neighbours.items() if len(neighbours) == 2]
    return reduce(int.__mul__, corner_tiles)


def second_star(tiles_input):
    tiles = parse_tiles_input(tiles_input)
    tile_to_neighbours = find_neighbours(tiles)

    world_map = {}
    tiles_in_world_map = {}
    i = 0
    for tile_id, neighbours in tile_to_neighbours.items():
        if len(neighbours) == 2:  # first corner
            if i != 2:
                i += 1
                continue
            area, borders = tiles[tile_id]
            world_map[(0, 0)] = area
            tiles_in_world_map[tile_id] = (0, 0)
            break

    while len(tiles_in_world_map) != len(tile_to_neighbours):

        for tile_id, coord in list(tiles_in_world_map.items()):
            neighbours = tile_to_neighbours[tile_id]
            _, parent_borders = tiles[tile_id]

            for neighbour in neighbours:
                if neighbour in tiles_in_world_map:
                    continue

                print("===== START =======")

                n_area, n_borders = tiles[neighbour]
                draw_world({(0, 0): n_area})
                direction, rotate_angle, flip_axis = find_required_action(parent_borders, n_borders)

                new_area = perform_area_actions(n_area, rotate_angle, flip_axis)
                tiles[neighbour] = (new_area, find_borders(new_area))

                new_coord = tuple([sum(coords) for coords in zip(direction, tiles_in_world_map[tile_id])])

                if new_coord in world_map:
                    print("!!!!! ", new_coord, direction, rotate_angle, flip_axis)
                    exit(-1)

                tiles_in_world_map[neighbour] = new_coord

                world_map[new_coord] = new_area

                draw_world(world_map)
                # print(f"{tile_id}:{coord} - {neighbour}:{new_coord}", rotate_angle, flip_axis)
                print("===== END ====== \n\n\n")

    draw_world(world_map)


def find_common_borders(borders1: Borders, borders2: Borders): return tuple(
    sorted(borders1.to_set() & borders2.to_set(), key=borders1.to_list().index))


def find_required_action(borders1: Borders, borders2: Borders):
    common_borders = find_common_borders(borders1, borders2)
    directions = {"top": (0, 1), "right": (1, 0), "bottom": (0, -1), "left": (-1, 0)}
    direction1, = [direction for direction in directions.keys() if getattr(borders1, direction) == common_borders]

    opposites = {"top": "bottom", "bottom": "top", "left": "right", "right": "left"}

    flip_axis = None
    direction2 = None

    for direction in directions.keys():
        border = getattr(borders2, direction)
        if border == common_borders:
            direction2 = direction
        elif border[::-1] == common_borders:
            direction2 = direction
            flip_axis = 1 if direction2 in ["top", "bottom"] else 0

    print("BEFORE MAGIC", direction1, direction2, common_borders, flip_axis, borders1, borders2)
    if direction1 == direction2:
        angle_to_rotate = 180
        if flip_axis is None:
            flip_axis = 1 if direction2 in ["top", "bottom"] else 0
        else:
            flip_axis = None

    elif opposites[direction1] == direction2:
        angle_to_rotate = 0

    else:
        hack = list(directions.keys())
        i1 = hack.index(opposites[direction1])
        i2 = hack.index(direction2)

        angle_to_rotate = (i2 - i1) * 90

        if angle_to_rotate in [-270, 270]:
            if flip_axis is None:
                flip_axis = 1 if direction2 in ["top", "bottom"] else 0
            else:
                flip_axis = None

    print("AFTER MAGIC", direction1, direction2, angle_to_rotate, flip_axis)
    return directions[direction1], angle_to_rotate, flip_axis


def perform_area_actions(area: Area, angle_to_rotate, flip_axis) -> Area:
    rotate_n = angle_to_rotate // 90
    array = np.array(area)
    if flip_axis is not None:
        array = np.flip(array, axis=flip_axis)

    array = np.rot90(array, rotate_n)
    return array.tolist()


def find_neighbours(tiles: typing.Dict[Id, typing.Tuple[Area, Borders]]) -> typing.DefaultDict[Id, typing.List[Id]]:
    tile_to_neighbours = defaultdict(list)

    for tile_id, (_, borders) in tiles.items():

        for tile2_id, (_, borders2) in tiles.items():
            common_borders = borders.to_set() & borders2.to_set()
            if common_borders and tile_id != tile2_id:
                tile_to_neighbours[tile_id].append(tile2_id)

    return tile_to_neighbours


def parse_tiles_input(tiles_input: typing.List[str]) -> typing.Dict[Id, typing.Tuple[Area, Borders]]:
    return {int(tile_id[5:-1]): ([list(a) for a in area], find_borders(area))
            for tile_id, *area in
            [single_area.split("\n") for single_area in tiles_input]
            }


def find_borders(tile_lines: Area) -> Borders:
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


def draw_world(world_map: typing.Dict[Coord, Area]):
    coords = list(sorted(world_map.keys(), key=lambda element: (-element[1], element[0])))
    columns = {coord[1]: None for coord in coords}.keys()
    rows = {coord[0]: None for coord in coords}.keys()

    print(coords)
    for col in columns:
        single_row_areas = [world_map.get((row, col), [" "] * 11) for row in rows]
        area_rows = list(zip(*single_row_areas))
        for row in area_rows:
            print(" ".join(["".join(a) for a in row]))

        print("")

    # for col in columns:
    #     print(col)
    #     print(" ".join([str(row) for row in rows]))
    #     print(" ".join([str(row) for row in rows if (row, col) in coords ]))
    #     print()


if __name__ == "__main__":
    tiles_input = open('src/main/resources/day20/input.txt', 'r').read().split("\n\n")
    print(first_star(tiles_input))
    print(second_star(tiles_input))
