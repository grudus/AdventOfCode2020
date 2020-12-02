import os
import re

def first_star(password_list):
    password_policy = [re.findall(r'(\d+)-(\d+) (\w): (\w+)', pswd) for pswd in password_list] 
    valid_passwords = [x for x in password_policy if len(x) > 0 and is_valid_toboggan(x[0])]
    return len(valid_passwords)


def second_star(password_list):
    password_policy = [re.findall(r'(\d+)-(\d+) (\w): (\w+)', pswd) for pswd in password_list] 
    valid_passwords = [x for x in password_policy if len(x) > 0 and is_valid_new_corporate_policies(x[0])]
    return len(valid_passwords)



def is_valid_toboggan(policy):
    (min, max, letter, pswd) = policy
    occurences = len([x for x in pswd if x == letter])
    return int(min) <= occurences <= int(max)


def is_valid_new_corporate_policies(policy):
    (min, max, letter, pswd) = policy
    return (pswd[int(min) - 1] == letter) ^ (pswd[int(max) - 1] == letter)

passwords = open(os.path.abspath(__file__ + '/../' + 'input.txt'), 'r').read().split("\n")

print(first_star(passwords))
print(second_star(passwords))
