from collections import defaultdict

def first_star(starting_numbers): return find_nth_spoken_number(starting_numbers, 2020)
def second_star(starting_numbers): return find_nth_spoken_number(starting_numbers, 30000000)

def find_nth_spoken_number(starting_numbers, n):
    occurences = defaultdict(list)
    for i, number in enumerate(starting_numbers): occurences[number] = [i + 1]
    prev_number = starting_numbers[-1]

    for turn in range(len(starting_numbers) + 1, n + 1):
        prev_occurences = occurences[prev_number]
        prev_number = 0 if len(prev_occurences) < 2 else prev_occurences[-1] - prev_occurences[-2]
        occurences[prev_number] += [turn]
    
    return prev_number


if __name__ == "__main__":
    starting_numbers = [int(x) for x in open('src/main/resources/day15/input.txt', 'r').read().split(",")]
    print(first_star(starting_numbers))
    print(second_star(starting_numbers))