import re

def first_star(passports):
    return len([passport for passport in passports if is_valid_passport(passport) ])


def is_valid_passport(passport):
    return has_required_keys(extract_keys(passport.split()))

def extract_keys(passport):
    return [pair.split(":")[0] for pair in passport]

def has_required_keys(password_key):
    return len([key for key in password_key if key != 'cid']) == 7


def second_star(passports):
    valid_passports = list(filter(is_valid_passport, passports))
    passport_maps = [create_passport_map(passport.split()) for passport in valid_passports]
    return len(list(filter(has_valid_values, passport_maps)))

def create_passport_map(passport):
    return {x.split(":")[0]: x.split(":")[1] for x in passport}

def has_valid_values(passport_map):
    return  (
        (1920 <= int(passport_map['byr']) <= 2002)
    and (2010 <= int(passport_map['iyr']) <= 2020)
    and (2020 <= int(passport_map['eyr']) <= 2030)
    and (has_valid_height(passport_map['hgt']))
    and (bool(re.match(r'^#(?:[0-9a-f]{6})$', passport_map['hcl'])))
    and (bool(re.match(r"amb|blu|brn|gry|grn|hzl|oth", passport_map['ecl'])))
    and (len(passport_map['pid']) == 9)
    )


def has_valid_height(height):
    parsed_data = re.findall(r'(\d+)(cm|in)', height)

    if len(parsed_data) == 0 or len(parsed_data[0]) < 2:
        return False

    (height, unit) = parsed_data[0]
    return unit == 'cm' if (150 <= int(height) <= 193) else (59 <= int(height) <= 76)


passports = open('src/main/resources/day04/input.txt', 'r').read().replace(",", "").split("\n\n")

# print(passports[0])

print(first_star(passports))
print(second_star(passports))
