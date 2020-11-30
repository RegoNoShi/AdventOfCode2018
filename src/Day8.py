
puzzle = [int(n.strip()) for n in open("../inputs/Day8.txt", "r").readline().split(" ")]


def node_value(_child_values, _metadata):
    if len(_child_values) == 0:
        return sum(_metadata)
    return sum([_child_values[_m - 1] for _m in _metadata if _m <= len(_child_values)])


metadata_sum = 0
stack = []
while len(puzzle) > 0:
    if len(stack) == 0 or stack[len(stack) - 1][0] != 0:
        stack.append((puzzle[0], puzzle[1], puzzle[0], []))
        puzzle = puzzle[2:]
    else:
        while len(stack) > 0 and stack[len(stack) - 1][0] == 0:
            _, metadata_count, child_num, child_values = stack[len(stack) - 1]
            stack = stack[:-1]
            metadata = puzzle[0:metadata_count]
            metadata_sum += sum(metadata)
            puzzle = puzzle[metadata_count:]
            node_val = node_value(child_values, metadata)
            if len(stack) > 0:
                stack[len(stack) - 1] = (stack[len(stack) - 1][0] - 1, stack[len(stack) - 1][1],
                                         stack[len(stack) - 1][2], stack[len(stack) - 1][3] + [node_val])

expected_output_part1 = 44338
output_part1 = metadata_sum
if output_part1 == expected_output_part1:
    print(f"✅ Challenge Part 1 -> {output_part1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part1}, got {output_part1}")

expected_output_part2 = 37560
output_part2 = node_val
if output_part2 == expected_output_part2:
    print(f"✅ Challenge Part 2 -> {output_part2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part2}, got {output_part2}")
