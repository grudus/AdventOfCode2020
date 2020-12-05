
def first_star(boarding_passes):
    positions = [calculate_position(boarding_pass) for boarding_pass in boarding_passes]
    return max([calculate_id(position) for position in positions])


def second_star(boarding_passes):
    positions = [calculate_position(boarding_pass) for boarding_pass in boarding_passes]
    position_ids = sorted(map(calculate_id, positions))

    previous_id = position_ids[0]
    for position_id in position_ids[1:]:

        if position_id != (previous_id + 1):
            return position_id - 1
        
        previous_id = position_id


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
