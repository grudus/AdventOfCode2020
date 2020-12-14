import re
from collections import defaultdict
from functools import reduce

def first_star(instructions): return sum_memory_values(instructions, update_single_registry)
def second_star(instructions): return sum_memory_values(instructions, update_multiple_registers)

def sum_memory_values(instructions, update_memory_func):
    memory = defaultdict(int)

    for instruction in instructions:
        if instruction.startswith("mask"):
            mask = instruction.split(" = ")[1]
            continue

        register, value = re.findall('mem.(\\d+).\\s+=\\s+(.*)', instruction)[0]
        update_memory_func(memory, mask, register, value)
    
    return sum(memory.values())

def update_single_registry(memory, mask, register, value):
    memory[int(register)] = int(apply_mask(mask, to_binary(value)), 2)

def apply_mask(mask, binary):
    new_value = list(mask)
    for i in range(len(mask)):
        if mask[i] == 'X':
            new_value[i] = binary[i]
    return "".join(new_value)


def update_multiple_registers(memory, mask, register, value):
    all_registers = apply_mask_and_find_all_registers(mask, to_binary(register))
        
    for binary_register in all_registers:
        memory[int("".join(binary_register), 2)] = int(value)

def apply_mask_and_find_all_registers(mask, binary):
    initial_register = list(binary)
    for i in range(len(mask)):
        if mask[i] in ['X', '1']:
            initial_register[i] = mask[i]
    
    return find_all_registers([initial_register])

def find_all_registers(registers):
    incomplete_registers = [register for register in registers if 'X' in register]
    if len(incomplete_registers) == 0:
        return registers

    handle_floating = lambda reg: [replace(reg, reg.index('X'), '0'), replace(reg, reg.index('X'), '1')]
    return find_all_registers(flat_map(incomplete_registers, handle_floating))


def to_binary(value, len=36): return format(int(value), f"0{len}b")
def flat_map(list_of_lists, func): return reduce(list.__add__, map(func, list_of_lists))

def replace(list, index, value):
    copy = list[:]
    copy[index] = value
    return copy


if __name__ == "__main__":
    instructions = open('src/main/resources/day14/input.txt', 'r').read().split("\n")
    print(first_star(instructions))
    print(second_star(instructions))