from copy import deepcopy

def first_star(seat_layout): return change_seats_and_stabilize_chaos(seat_layout, count_neighbours, 4)
def second_star(seat_layout): return change_seats_and_stabilize_chaos(seat_layout, count_seen_occupied_seats, 5)

def change_seats_and_stabilize_chaos(initial_layout, count_occupied_seats_func, max_occupied_seats):
    curr_layout = deepcopy(initial_layout)
    while True:
        new_layout, changed = change_seats(deepcopy(curr_layout), count_occupied_seats_func, max_occupied_seats)
        if not changed:
            return count_occupied_seats(curr_layout)
        curr_layout = new_layout


def change_seats(layout, count_occupied_seats_func, max_occupied_seats):
    layout_after_changes = deepcopy(layout)
    changed = False
    positions = [(row, col) for row in range(len(layout)) for col in (range(len(layout[0]))) if layout[row][col] != '.']

    for row, col in positions:
        occupied_seats = count_occupied_seats_func(layout, row, col)
        
        if occupied_seats == 0:
            changed = changed or layout[row][col] != '#'
            layout_after_changes[row][col] = '#'
        elif occupied_seats >= max_occupied_seats:
            changed = changed or layout[row][col] != 'L'
            layout_after_changes[row][col] = 'L'
    
    return (layout_after_changes, changed)


def count_neighbours(seat_layout, row, col):
    max_row = len(seat_layout)
    max_col = len(seat_layout[0])

    neighbours = [seat_layout[r][c] 
    for r in [row-1, row, row+1] 
    for c in [col-1, col, col+1] 
    if r >= 0 and r < max_row and c >= 0 and c < max_col and (r, c) != (row, col)
    ]

    return "".join(neighbours).count("#")


def count_seen_occupied_seats(seat_layout, row, col):
    max_row = len(seat_layout)
    max_col = len(seat_layout[0])

    fields_to_check = [
        [y[col] for y in seat_layout[0:row]][::-1],  #N
        [seat_layout[row-i][col+i] for i in range(1, max_row) if row-i >= 0 and col+i < max_col], #NE
        seat_layout[row][col + 1:max_col], #E
        [seat_layout[row+i][col+i] for i in range(1, max_row) if row+i < max_row and col+i < max_col], #SE
        [y[col] for y in seat_layout[row+1:max_row]], #S
        [seat_layout[row+i][col-i] for i in range(1, max_row) if row+i < max_row and col-i >= 0], #SW
        (seat_layout[row][0:col])[::-1], #W
        [seat_layout[row-i][col-i] for i in range(1, max_row) if row-i >= 0 and col-i >= 0], #NW
    ]

    count = 0

    for fields in fields_to_check:
        seats = "".join(fields)
        first_occupied_seat = seats.find("#")
        first_empty_seat = seats.find("L")

        if first_occupied_seat == -1: continue
        if first_empty_seat == -1 or first_occupied_seat < first_empty_seat: count += 1

    return count


def count_occupied_seats(layout): return sum(["".join(x).count("#") for x in layout])


if __name__ == "__main__":
    seat_layout = open('src/main/resources/day11/input.txt', 'r').read().split("\n")
    seat_layout = [list(row) for row in seat_layout]
    print(first_star(seat_layout))
    print(second_star(seat_layout))