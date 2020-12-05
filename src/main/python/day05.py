
def first_star(boarding_passes):
    positions = map(calculate_position, boarding_passes)
    return max(map(calculate_id, positions))


def second_star(boarding_passes):
    positions = map(calculate_position, boarding_passes)
    position_ids = sorted(map(calculate_id, positions))

    return next(filter(lambda id: id - 1 not in position_ids, position_ids[1:])) - 1


def calculate_id(tuple):
    return tuple[0] * 8 + tuple[1]

def calculate_position(boarding_pass):
    return (convert_to_binary(boarding_pass[:7]), convert_to_binary(boarding_pass[7:]))

def convert_to_binary(position_stirng):
    binary_list = ["1" if position in ['B', 'R'] else "0" for position in position_stirng]
    return int("".join(binary_list) ,2)


if __name__ == "__main__":
    boarding_passes = open('src/main/resources/day05/input.txt', 'r').read().split("\n")
    print(first_star(boarding_passes))
    print(second_star(boarding_passes))
