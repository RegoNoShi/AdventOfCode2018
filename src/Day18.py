
puzzle = [str(line.strip()) for line in open("../inputs/Day18.txt", "r").readlines()]

offsets = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]


def adjacent_acres(_area, _r, _c):
    _ground, _trees, _lumberyard = 0, 0, 0
    for rD, cD in offsets:
        rf, cf = _r + rD, _c + cD
        if rf < 0 or rf >= len(_area) or cf < 0 or cf >= len(_area[_r]):
            continue
        if _area[rf][cf] == '.':
            _ground += 1
        elif _area[rf][cf] == '|':
            _trees += 1
        else:
            _lumberyard += 1
    return _ground, _trees, _lumberyard


def solve(_puzzle, minutes):
    area = _puzzle
    previous_area_states = {}
    minute = 1
    while minute <= minutes:
        next_area = []
        area_state = ''
        for r in range(len(area)):
            next_area.append([])
            for c in range(len(area[r])):
                ground, trees, lumberyard = adjacent_acres(area, r, c)
                if area[r][c] == '.' and trees >= 3:
                    next_area[r].append('|')
                elif area[r][c] == '|' and lumberyard >= 3:
                    next_area[r].append('#')
                elif area[r][c] == '#' and (trees == 0 or lumberyard == 0):
                    next_area[r].append('.')
                else:
                    next_area[r].append(area[r][c])
            area_state += ''.join(next_area[r])
        if area_state in previous_area_states:
            minute = minutes - (minutes - previous_area_states[area_state]) % (minute - previous_area_states[area_state])
        else:
            previous_area_states[area_state] = minute
        area = next_area
        minute += 1

    lumberyards = 0
    wooded = 0
    for r in range(len(area)):
        for c in range(len(area[r])):
            if area[r][c] == '|':
                wooded += 1
            elif area[r][c] == '#':
                lumberyards += 1

    return lumberyards * wooded


output_part_1 = solve(puzzle, 10)
expected_output_part_1 = 466125
if output_part_1 == expected_output_part_1:
    print(f"✅ Challenge Part 1 -> {output_part_1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part_1}, got {output_part_1}")

output_part_2 = solve(puzzle, 1000000000)
expected_output_part_2 = 207998
if output_part_2 == expected_output_part_2:
    print(f"✅ Challenge Part 2 -> {output_part_2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part_2}, got {output_part_2}")
