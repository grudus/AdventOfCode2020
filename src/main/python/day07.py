import re

def first_star(rule_list):
    rule_map = dict([create_rule_map(rule) for rule in rule_list])
    my_bag_holders = find_my_bag_holders(rule_map, "shiny gold")
    return len(my_bag_holders)
    

def create_rule_map(rule):
    [key, rest] = rule.split("contain")
    contained_bags = re.sub(r"\d+ |\.| bags?", "", rest).strip().split(", ")
    return (key.strip().replace(" bags", ""), contained_bags)


def find_my_bag_holders(rule_map, my_bag_color):
    my_bag_holders = []
    rule_map = rule_map.copy()
    while True:
        to_remove = []
        if len(rule_map) == 0:
            break

        for bag, contained_bags in rule_map.items():
            if (my_bag_color in contained_bags) or ( any([True if x in my_bag_holders else False for x in contained_bags])  ):
                my_bag_holders.append(bag)
                to_remove.append(bag)
            if (bag == 'no other'):
                to_remove.append(bag)
        
        if len(to_remove) == 0:
            break 

        [rule_map.pop(k, None) for k in to_remove]
    
    return my_bag_holders


def second_star(rule_list):
    rule_map = dict([create_rule_map_2(rule) for rule in rule_list])
    colors_to_check = ["shiny gold"]
    for x, y in rule_map.items():
        print(x, y)

    return count_bags(rule_map, colors_to_check, 1) - 1


def count_bags(rule_map, colors_to_check, result):
    print("count_bags", colors_to_check, result)
    if len(colors_to_check) == 0:
        return result
    
    bags_with_count = rule_map[colors_to_check[0]]
    colors_to_check = colors_to_check[1:]

    xx = 0
    for (count, bag) in bags_with_count:
        print("FOR", count, bag)
        if count == 0:
            return result
        
        xx += count * count_bags(rule_map, [bag], result)

    return result + xx

    



def create_rule_map_2(rule):
    [key, rest] = rule.split("contain")
    contained_bags = re.sub(r"\.| bags?", "", rest).strip().split(", ")
    dupa = [(''.join(filter(str.isdigit, x)), re.sub(r"\d+", "", x).strip()) for x in contained_bags]
    xx = [(int(x) if len(x) > 0 else 0, y) for (x, y) in dupa]
    return (key.strip().replace(" bags", ""), xx)


if __name__ == "__main__":
    rules = open('src/main/resources/day07/input.txt', 'r').read().split("\n")
    # print(first_star(rules))
    print(second_star(rules))
