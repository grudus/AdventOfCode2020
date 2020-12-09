import itertools

def first_star(xmas_messages):
    preamble = 25
    xmas_to_check_sum = [(xmas_messages[i-preamble:i], xmas_messages[i]) for i in range(preamble, len(xmas_messages))]
    sums_for_xmas = [(find_sums(previous_n, 2), xmas) for (previous_n, xmas) in xmas_to_check_sum]
    return [xmas for (sums, xmas) in sums_for_xmas if xmas not in sums][0]


def find_sums(number_list, n):
    return list(map(sum, list(itertools.combinations(number_list, n))))


def second_star(xmas_messages):
    invalid_xmas = first_star(xmas_messages)

    for i in range(len(xmas_messages)):
       for j in range(i + 1, len(xmas_messages)):
           xmas_range = xmas_messages[i:j]
           sum_to_check = sum(xmas_range)
           if (sum_to_check > invalid_xmas):
               break
           if sum_to_check == invalid_xmas:
                return min(xmas_range) + max(xmas_range)


if __name__ == "__main__":
    xmas_messages = open('src/main/resources/day09/input.txt', 'r').read().split("\n")
    xmas_messages = list(map(int, xmas_messages))
    print(first_star(xmas_messages))
    print(second_star(xmas_messages))
