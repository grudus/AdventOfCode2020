import itertools
from operator import mul
from functools import reduce


def first_star(expense_report):
    combined = list(itertools.combinations(expense_report, 2))
    matching_pairs = [pair for pair in combined if sum(list(pair)) == 2020]
    return reduce(mul, matching_pairs[0])


def second_star(expense_report):
    combined = list(itertools.combinations(expense_report, 3))
    matching_pairs = [pair for pair in combined if sum(list(pair)) == 2020]
    return reduce(mul, matching_pairs[0])





report = open('src/main/resources/day01/input.txt', 'r').read()
numbers = list(map(int, report.split("\n")))

print(first_star(numbers))
print(second_star(numbers))
