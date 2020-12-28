def first_star(cups):
    current_cup = cups[0]
    for _ in range(100): cups, current_cup = make_move(cups[:], current_cup)
    return calculate_score(cups)


def make_move(cups, current_cup):
    normalize_dest = lambda x: x if x >= min(cups) else max(cups)

    current_index = cups.index(current_cup)
    picked = []
    index_to_pick = current_index + 1

    while len(picked) != 3:
        index_to_pick = index_to_pick % len(cups)
        picked.append(cups[index_to_pick])
        del cups[index_to_pick]

    destination = normalize_dest(current_cup - 1)
    while destination in picked: destination = normalize_dest(destination - 1)
    destination_index = cups.index(destination)
    
    picked = list(reversed(picked))
    for index_to_pick in range(destination_index+1, destination_index+4):
        cups.insert(index_to_pick, picked.pop())

    return cups, cups[(cups.index(current_cup) + 1) % len(cups)]


def calculate_score(cups):
    starting_index = cups.index(1)
    rearranged_cups = (cups + cups)[starting_index + 1:starting_index + len(cups)]
    return "".join(map(str, rearranged_cups))



if __name__ == "__main__":
    cups = list(open('src/main/resources/day23/input.txt', 'r').read())
    cups = [int(cup) for cup in cups]
    print(first_star(cups[:]))
    # print(second_star(player1_deck, player2_deck))