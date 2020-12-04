
import re

puzzle = [str(line.strip()) for line in open("../inputs/Day16.txt", "r").readlines()]

all_operations = {
    'addr': lambda registers, a, b: registers[a] + registers[b],
    'addi': lambda registers, a, b: registers[a] + b,
    'mulr': lambda registers, a, b: registers[a] * registers[b],
    'muli': lambda registers, a, b: registers[a] * b,
    'banr': lambda registers, a, b: registers[a] & registers[b],
    'bani': lambda registers, a, b: registers[a] & b,
    'borr': lambda registers, a, b: registers[a] | registers[b],
    'bori': lambda registers, a, b: registers[a] | b,
    'setr': lambda registers, a, _: registers[a],
    'seti': lambda registers, a, _: a,
    'gtir': lambda registers, a, b: 1 if a > registers[b] else 0,
    'gtri': lambda registers, a, b: 1 if registers[a] > b else 0,
    'gtrr': lambda registers, a, b: 1 if registers[a] > registers[b] else 0,
    'eqir': lambda registers, a, b: 1 if a == registers[b] else 0,
    'eqri': lambda registers, a, b: 1 if registers[a] == b else 0,
    'eqrr': lambda registers, a, b: 1 if registers[a] == registers[b] else 0
}

line_number = 0
output_part_1 = 0
number_to_operations = {opcode: set(all_operations.keys()) for opcode in range(16)}
while True:
    if line_number > len(puzzle) or len(puzzle[line_number]) == 0:
        break
    before_match = re.search(r"Before:\s\[(\d+),\s(\d+),\s(\d+),\s(\d+)]", puzzle[line_number])
    parameters_match = re.search(r"(\d+)\s(\d+)\s(\d+)\s(\d+)", puzzle[line_number + 1])
    after_match = re.search(r"After:\s\s\[(\d+),\s(\d+),\s(\d+),\s(\d+)]", puzzle[line_number + 2])
    initial_state = [int(before_match[1]), int(before_match[2]), int(before_match[3]), int(before_match[4])]
    parameters = [int(parameters_match[1]), int(parameters_match[2]), int(parameters_match[3]), int(parameters_match[4])]
    final_state = [int(after_match[1]), int(after_match[2]), int(after_match[3]), int(after_match[4])]
    line_number += 4

    count_operations = 0
    operations = set()
    for name, operation in all_operations.items():
        state = initial_state.copy()
        state[parameters[3]] = operation(initial_state, parameters[1], parameters[2])

        if state == final_state:
            count_operations += 1
            operations.add(name)

    if count_operations >= 3:
        output_part_1 += 1
    number_to_operations[parameters[0]] = number_to_operations[parameters[0]].intersection(operations)

expected_output_part_1 = 570
if output_part_1 == expected_output_part_1:
    print(f"✅ Challenge Part 1 -> {output_part_1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part_1}, got {output_part_1}")

number_to_operation = {}
while len(number_to_operations) > 0:
    for opcode in number_to_operations.keys():
        if len(number_to_operations[opcode]) == 1:
            operation = number_to_operations[opcode].pop()
            del number_to_operations[opcode]
            number_to_operation[opcode] = operation
            for operations in number_to_operations.values():
                if operation in operations:
                    operations.remove(operation)
            break

line_number += 3
state = [0, 0, 0, 0]
while line_number < len(puzzle):
    parameters_match = re.search(r"(\d+)\s(\d+)\s(\d+)\s(\d+)", puzzle[line_number])
    parameters = [int(parameters_match[1]), int(parameters_match[2]), int(parameters_match[3]), int(parameters_match[4])]
    operation = all_operations[number_to_operation[parameters[0]]]
    state[parameters[3]] = operation(state, parameters[1], parameters[2])
    line_number += 1

output_part_2 = state[0]
expected_output_part_2 = 503
if output_part_2 == expected_output_part_2:
    print(f"✅ Challenge Part 2 -> {output_part_2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part_2}, got {output_part_2}")
