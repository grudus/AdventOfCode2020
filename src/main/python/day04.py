import re

def first_star(passports):
    return len([passport for passport in passports if is_valid_passport(passport) ])

def second_star(passports):
    valid_passports = list(filter(is_valid_passport, passports))
    passport_maps = [create_passport_map(passport.split()) for passport in valid_passports]
    return len(list(filter(has_valid_values, passport_maps)))


def is_valid_passport(passport):
    return has_required_keys(extract_keys(passport.split()))

def extract_keys(passport):
    return [pair.split(":")[0] for pair in passport]

def has_required_keys(password_key):
    return len([key for key in password_key if key != 'cid']) == 7

def create_passport_map(passport):
    return {x.split(":")[0]: x.split(":")[1] for x in passport}

def has_valid_values(passport_map):
    return  (
        (1920 <= int(passport_map['byr']) <= 2002)
    and (2010 <= int(passport_map['iyr']) <= 2020)
    and (2020 <= int(passport_map['eyr']) <= 2030)
    and (has_valid_height(passport_map['hgt']))
    and (bool(re.match(r'^#([0-9a-f]{6})$', passport_map['hcl'])))
    and (passport_map['ecl'] in "amb blu brn gry grn hzl oth".split())
    and (bool(re.match(r'^[0-9]{9}$', passport_map['pid'])))
    )

def has_valid_height(height):
    if height[-2:] == 'cm':
        return 150 <= int(height[:-2]) <= 193
    elif height[-2:] == 'in':
        return 59 <= int(height[:-2]) <= 76
    else:
        return False


if __name__ == "__main__":
    passports = open('src/main/resources/day04/input.txt', 'r').read().split("\n\n")
    print(first_star(passports))
    print(second_star(passports))
