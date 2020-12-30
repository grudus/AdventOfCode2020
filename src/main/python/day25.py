def first_star(card_pk, door_pk):
    door_loop_size, _ = calculate_key(7, lambda _, value: value != door_pk)

    return calculate_key(card_pk, lambda loop_size, _: loop_size < door_loop_size)[1]

def calculate_key(subject_number, prediction):
    loop_size = 0
    value = 1
    while prediction(loop_size, value):
        value *= subject_number
        value %= 20201227
        loop_size += 1
    return (loop_size, value)

if __name__ == "__main__":
    card_pk, door_pk  = [int(key) for key in open('src/main/resources/day25/input.txt', 'r').read().split("\n")]
    print(first_star(card_pk, door_pk))