import re
import itertools
from functools import reduce

def first_star(rules, nearby_tickets):
    field_conditions = list(map(extract_field_and_condition, rules))
    return sum(find_invalid_numbers(field_conditions, nearby_tickets))

def second_star(rules, my_ticket, nearby_tickets):
    field_conditions = list(map(extract_field_and_condition, rules))
    tickets = find_valid_tickets(field_conditions, nearby_tickets)
    field_to_index = {}

    while len(field_to_index) != len(my_ticket):
        for column_index in range(len(rules)):
            column_numbers = [ticket[column_index] for ticket in tickets]
            valid_fields = [valid_fields for valid_fields, condition in field_conditions if valid_fields not in field_to_index.keys() and all(condition(number) for number in column_numbers)]
            if len(valid_fields) == 1:
                field_to_index[valid_fields[0]] = column_index
        
    departure_indexes = [index for field, index in field_to_index.items() if "departure" in field]    
    my_ticket_departures = [my_ticket[i] for i in departure_indexes]
    return reduce(lambda x, y: x * y, my_ticket_departures)


def extract_field_and_condition(rule):
    (field, from1, to1, from2, to2) = re.findall(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)', rule)[0]
    return field, lambda number: int(from1) <= number <= int(to1) or int(from2) <= number <= int(to2)


def find_invalid_numbers(field_conditions, nearby_tickets):
    return [number 
        for ticket in nearby_tickets 
        for number in ticket 
        if not any(condition(number) for _, condition in field_conditions)
    ] 

def find_valid_tickets(range_conditions, nearby_tickets):
    invalid_ticket_numbers = find_invalid_numbers(range_conditions, nearby_tickets)
    return [tickets for tickets in nearby_tickets if all(invalid not in tickets for invalid in invalid_ticket_numbers)]


if __name__ == "__main__":
    [rules, my_ticket, nearby_tickets]  = open('src/main/resources/day16/input.txt', 'r').read().split("\n\n")
    rules = rules.split("\n")
    nearby_tickets = [list(map(int, nearby.split(","))) for nearby in nearby_tickets.split("\n")[1:]]
    my_ticket = [int(number) for number in my_ticket.split("\n")[1].split(",")]
    print(first_star(rules, nearby_tickets))
    print(second_star(rules, my_ticket, nearby_tickets))