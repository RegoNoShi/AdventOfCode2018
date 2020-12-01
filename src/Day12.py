
import re

puzzle = open("../inputs/Day12.txt", "r").readlines()


def plant(_idx, _field, _rules):
    check = tuple([1 if c in _field else 0 for c in range(_idx - 2, _idx + 3)])
    if check in _rules:
        return _idx


def calculate_result(_puzzle, _generations):
    match = re.search(r"initial state:\s([\\.#]+)", _puzzle[0])
    initial_state = match.group(1)
    field = [idx for idx in range(len(initial_state)) if initial_state[idx] == '#']
    rules = set()
    for line in puzzle[1:]:
        match = re.search(r"([\\.#]+)\s=>\s([\\.#])", line)
        if match.group(2) == '#':
            rules.add(tuple(1 if c == '#' else 0 for c in match.group(1)))

    diff = None
    gen = None
    for gen in range(_generations):
        min_idx = min(field) - 5
        max_idx = max(field) + 5

        new_field = [plant(i, field, rules) for i in range(min_idx, max_idx) if plant(i, field, rules) is not None]
        if diff == sum(new_field) - sum(field):
            break
        diff = sum(new_field) - sum(field)
        field = new_field

    return sum(field) if gen == (_generations - 1) else sum(field) + (diff * (_generations - gen))


output_part_1 = calculate_result(puzzle, 20)
expected_output_part_1 = 3738
if output_part_1 == expected_output_part_1:
    print(f"✅ Challenge Part 1 -> {output_part_1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part_1}, got {output_part_1}")

output_part_2 = calculate_result(puzzle, 50000000000)
expected_output_part_2 = 3900000002467
if output_part_2 == expected_output_part_2:
    print(f"✅ Challenge Part 2 -> {output_part_2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part_2}, got {output_part_2}")
