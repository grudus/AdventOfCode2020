def first_star(instructions):
    return execute_code(list(map(parse_instruction, instructions)))[1]
    

def second_star(instructions):
    instructions = list(map(parse_instruction, instructions))

    for i, (operation, value) in enumerate(instructions):
        new_instructions = instructions.copy()

        if operation == 'jmp':
            new_instructions[i] = ('nop', value)
        elif operation == 'nop':
            new_instructions[i] = ('jmp', value)
        
        (execution_type, state) = execute_code(new_instructions)
        if execution_type == 'END':
            return state


def execute_code(parsed_instructions):
    global_state = 0
    current_line = 0
    executed_lines = set()
    all_lines = len(parsed_instructions)
    
    while True:
        (operation, value) = parsed_instructions[current_line]

        if operation == 'nop':
            current_line += 1
        elif operation == 'acc':
            current_line += 1
            global_state += value
        elif operation == 'jmp':
            current_line += value

        if (current_line in executed_lines):
            return ("LOOP", global_state)
        elif (current_line >= all_lines):
            return ("END", global_state)

        executed_lines.add(current_line)


def parse_instruction(instruction):
    operation = instruction[:3]
    value = instruction[4:]
    return (operation, int(value[1:]) if value[0] == '+' else -int(value[1:]))

if __name__ == "__main__":
    instructions = open('src/main/resources/day08/input.txt', 'r').read().split("\n")
    print(first_star(instructions))
    print(second_star(instructions))
