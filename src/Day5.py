
puzzle = open("../inputs/Day5.txt", "r").readline().strip()


def react(polymer):
    reaction = True
    while reaction:
        reaction = False
        tmp_polymer = ""
        i = 0
        while i < len(polymer):
            if i >= len(polymer):
                break
            if i == len(polymer) - 1:
                tmp_polymer += polymer[i]
                break
            if abs(ord(polymer[i]) - ord(polymer[i + 1])) != 32:
                tmp_polymer += polymer[i]
                i += 1
            else:
                i += 2
                reaction = True
        polymer = tmp_polymer
    return polymer


solution_part1 = react(puzzle)

expected_output_part1 = 11310
output_part1 = len(solution_part1)
if output_part1 == expected_output_part1:
    print(f"✅ Challenge Part 1 -> {output_part1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part1}, got {output_part1}")

output_part2 = len(solution_part1)
elements = set([c.lower() for c in solution_part1])
for element in elements:
    tmp_puzzle = solution_part1.replace(element, "")
    tmp_puzzle = tmp_puzzle.replace(element.upper(), "")
    tmp_puzzle = react(tmp_puzzle)
    if len(tmp_puzzle) < output_part2:
        output_part2 = len(tmp_puzzle)

expected_output_part2 = 6020
if output_part2 == expected_output_part2:
    print(f"✅ Challenge Part 2 -> {output_part2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part2}, got {output_part2}")
