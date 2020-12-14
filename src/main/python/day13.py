import math
from functools import reduce

def first_star(earliest_timestamp, bus_ids):
    bus_ids = [int(bus_id) for bus_id in bus_ids.split(",") if bus_id != 'x']
    buses_to_earliest_department = [(bus_id, earliest_timestamp // bus_id * bus_id + bus_id - earliest_timestamp) for bus_id in bus_ids]
    buses_to_earliest_department = sorted(buses_to_earliest_department, key = lambda x: x[1])
    return buses_to_earliest_department[0][0] * buses_to_earliest_department[0][1] 


def second_star(buses_ids):
    aritmetic_progressions = []
    
    for i, bus_id in enumerate(buses_ids.split(",")):
        if bus_id == 'x': continue
        aritmetic_progressions.append((-i, int(bus_id)))
    
    final_arithmetic_progression = reduce(find_intersection_progression, aritmetic_progressions)
    return final_arithmetic_progression[0] - final_arithmetic_progression[1]


# weird math stuff https://math.stackexchange.com/questions/1656120/formula-to-find-the-first-intersection-of-two-arithmetic-progressions
def find_intersection_progression(ar1, ar2):
    a1, d = ar1
    b1, D = ar2

    c = a1 - b1 + D - d
    g = math.gcd(d, D)
    u, v = extended_gcd(-d, D)

    t = min(int(-c/D * u) + 1, int(-c/d * v) + 1)
    n = int((c/g) * u + t * (D/g))
    X = int(a1 + (n - 1) * d)

    return (X, math.lcm(d, D))


def extended_gcd(a, b):
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)
    
    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)

    return (old_s, old_t)
        


if __name__ == "__main__":
    lines = open('src/main/resources/day13/input.txt', 'r').read().split("\n")
    print(first_star(int(lines[0]), lines[1]))
    print(second_star(lines[1]))