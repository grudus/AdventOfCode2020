
def first_star(boarding_passes):
    positions = [calculate_position(boarding_pass) for boarding_pass in boarding_passes]
    return max([row * 8 + col for (row, col) in positions])


def calculate_position(boarding_pass):
    rows = boarding_pass[:7]
    cols = boarding_pass[7:]

    return (convert_to_binary(rows), convert_to_binary(cols))

def convert_to_binary(position_stirng):
    binary_list = ["1" if position in ['B', 'R'] else "0" for position in position_stirng]
    return int("".join(binary_list) ,2)



if __name__ == "__main__":
    boarding_passes = open('src/main/resources/day05/input.txt', 'r').read().split("\n")
    print(first_star(boarding_passes))
    # print(second_star(boarding_passes))
