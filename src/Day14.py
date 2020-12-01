
puzzle = '047801'
int_puzzle = int(puzzle)
array_puzzle = [int(c) for c in puzzle]
scores = [3, 7]
pos = [0, 1]
output_part_1 = None
output_part_2 = None

while output_part_1 is None or output_part_2 is None:
    score = scores[pos[0]] + scores[pos[1]]
    if score >= 10:
        scores.append(score // 10)
    scores.append(score % 10)
    pos = [(p + scores[p] + 1) % len(scores) for p in pos]

    if output_part_1 is None and len(scores) >= (int_puzzle + 10):
        output_part_1 = ''.join([str(s) for s in scores[int_puzzle: int_puzzle + 10]])

    if output_part_2 is None:
        if len(scores) >= len(puzzle) and array_puzzle == scores[-len(puzzle):]:
            output_part_2 = len(scores) - len(puzzle)
        elif score >= 10 and len(scores) > len(puzzle) and array_puzzle == scores[-(len(puzzle) + 1):-1]:
            output_part_2 = len(scores) - len(puzzle) - 1

expected_output_part_1 = '1342316410'
if output_part_1 == expected_output_part_1:
    print(f"✅ Challenge Part 1 -> {output_part_1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part_1}, got {output_part_1}")

expected_output_part_2 = 20235230
if output_part_2 == expected_output_part_2:
    print(f"✅ Challenge Part 2 -> {output_part_2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part_2}, got {output_part_2}")
