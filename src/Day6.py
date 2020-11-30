
puzzle = list(map(lambda box_id: box_id, open("../inputs/Day6.txt", "r").readlines()))


def line_to_coordinates(idx, line):
    coord = line.split(", ")
    return int(coord[0]), int(coord[1]), idx


def min_distance(x, y, _coordinates):
    min_dist = float('inf')
    result = None
    accumulator = 0
    for coord in _coordinates:
        d = abs(x - coord[0]) + abs(y - coord[1])
        accumulator += d
        if d < min_dist:
            min_dist = d
            result = coord[2]
        elif d == min_dist:
            result = -1
    return result, accumulator


coordinates = list(map(lambda idx: line_to_coordinates(idx, puzzle[idx]), range(len(puzzle))))

max_x = max([x for x, _, _ in coordinates])
max_y = max([y for _, y, _ in coordinates])

field = [[-1]] * max_x
counter = [0] * len(coordinates)
infinite = [False] * len(coordinates)
limit = 10000
less_than_limit = 0
for x in range(max_x):
    field[x] = [-1] * max_y
    for y in range(max_y):
        (res, total) = min_distance(x, y, coordinates)
        if total < limit:
            less_than_limit += 1
        if res >= 0:
            field[x][y] = res
            counter[field[x][y]] += 1
            if x == 0 or y == 0 or x == (max_x - 1) or y == (max_y - 1):
                infinite[field[x][y]] = True

expected_output_part1 = 3260
output_part1 = max([counter[idx] for idx in range(len(coordinates)) if infinite[idx] is False])
if output_part1 == expected_output_part1:
    print(f"✅ Challenge Part 1 -> {output_part1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part1}, got {output_part1}")

expected_output_part2 = 42535
output_part2 = less_than_limit
if output_part2 == expected_output_part2:
    print(f"✅ Challenge Part 1 -> {output_part2}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part2}, got {output_part2}")
