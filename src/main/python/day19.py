import re
import typing

def first_star(rules, messages): return find_matching_messages(rules, messages)
def second_star(rules, messages): return find_matching_messages(rules, messages, rules_mapper=extend_8_11)


def find_matching_messages(rules: typing.List[str], messages: typing.List[str],
                           rules_mapper: typing.Callable[[typing.Dict[str, str]], typing.Dict[str, str]] = lambda x: x):
    rules_regex = find_rules_regex(rules, rules_mapper)
    regex = re.compile('^' + rules_regex["0"] + "$")
    return sum([1 for message in messages if regex.match(message)])


def find_rules_regex(rules: typing.List[str],
                     rules_mapper: typing.Callable[[typing.Dict[str, str]], typing.Dict[str, str]]):
    rules: typing.Dict[str, str] = {rule_id: valid_rules.replace('"', '')
                                    for rule_id, valid_rules in [rule.split(": ") for rule in rules]
                                    }

    rules = rules_mapper(rules.copy())
    rules_regex = {}

    while rules:
        for rule_id, valid_rules in list(rules.items()):
            if valid_rules in ['a', 'b']:
                rules_regex[rule_id] = valid_rules
                del rules[rule_id]
                continue

            sub_rules = [rule.split() for rule in valid_rules.split("|")]
            all_sub_rules_known = all([all(rule in rules_regex for rule in rules) for rules in sub_rules])

            if not all_sub_rules_known: continue

            sub_regexes = ["".join([rules_regex[rule] for rule in sub_rule]) for sub_rule in sub_rules]
            rules_regex[rule_id] = "(" + "|".join(sub_regexes) + ")"
            del rules[rule_id]

    return rules_regex


def extend_8_11(rules: typing.Dict[str, str]):
    rules["8"] = "42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42"
    rules["11"] = "42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31"
    return rules


if __name__ == "__main__":
    rules, messages = open('src/main/resources/day19/input.txt', 'r').read().split("\n\n")
    rules, messages = rules.split("\n"), messages.split("\n")
    print(first_star(rules, messages))
    print(second_star(rules, messages))
