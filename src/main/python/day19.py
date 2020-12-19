from collections import defaultdict
import itertools

def first_star(rules, messages):
    rule_map = find_rule_map(rules)
    return sum([1 for message in messages if message in rule_map["0"]])


def find_rule_map(rules):
    rule_map = defaultdict(list)
    rules = [(rule.split(": ")[0], rule.split(": ")[1].replace('"', '')) for rule in rules]

    while rules:
        for rule_entry in rules[:]:
            rule_number, valid_rules = rule_entry

            if valid_rules in ['a', 'b']:
                rule_map[rule_number] = [valid_rules]
                rules.remove(rule_entry)
                continue

            elif all(rule in rule_map for rule in valid_rules.replace("|", "").split()):     
                rules.remove(rule_entry)
                possible_patterns = [rules.split() for rules in valid_rules.split("|")]

                for rule_pattern in possible_patterns:
                    result = [rule_map[rule] for rule in rule_pattern] 
                    all_possible_values = itertools.product(*result)
                    all_possible_values = ["".join(value) for value in all_possible_values]     
                    rule_map[rule_number] += all_possible_values
    
    return rule_map


if __name__ == "__main__":
    rules, messages = open('src/main/resources/day19/input.txt', 'r').read().split("\n\n")
    rules, messages = rules.split("\n"), messages.split("\n")
    print(first_star(rules, messages))