
import re

puzzle = [str(line.strip()) for line in open("../inputs/Day17.txt", "r").readlines()]


def water_fall(_pos, _clay, _water, _max_y):
    while True:
        if _pos[1] + 1 > _max_y:
            return []

        _next_pos = (_pos[0], _pos[1] + 1)
        if _next_pos not in _clay and _next_pos not in _water:
            _water.add(_next_pos)
            _pos = _next_pos
        else:
            break

    _new_spring_points = []
    _left_limit = None
    _right_limit = None
    while True:
        _bottom_pos = _pos
        while True:
            _down_pos = (_pos[0], _pos[1] + 1)
            if _down_pos not in _clay:
                _border_pos = (_down_pos[0] + 1, _down_pos[1])
                if _border_pos in _clay:
                    _new_spring_points.append(_pos)
                break

            _next_pos = (_pos[0] - 1, _pos[1])
            if _next_pos in _clay:
                _left_limit = _pos[0]
                break
            else:
                _pos = _next_pos

        _pos = _bottom_pos
        while True:
            _down_pos = (_pos[0], _pos[1] + 1)

            if _down_pos not in _clay:
                _border_pos = (_down_pos[0] - 1, _down_pos[1])
                if _border_pos in _clay:
                    _new_spring_points.append(_pos)
                break

            _next_pos = (_pos[0] + 1, _pos[1])
            if _next_pos in _clay:
                _right_limit = _pos[0]
                break
            else:
                _pos = _next_pos

        if len(_new_spring_points) == 2:
            for _x in range(_new_spring_points[0][0], _new_spring_points[1][0] + 1):
                _water.add((_x, _new_spring_points[1][1]))
            break
        elif _left_limit is not None and _right_limit is not None:
            for _x in range(_left_limit, _right_limit + 1):
                _water.add((_x, _pos[1]))
                _clay.add((_x, _pos[1]))
            _pos = (_bottom_pos[0], _bottom_pos[1] - 1)
            _left_limit = None
            _right_limit = None
        elif len(_new_spring_points) == 1 and _left_limit is not None:
            for _x in range(_left_limit, _new_spring_points[0][0] + 1):
                _water.add((_x, _pos[1]))
            break
        elif len(_new_spring_points) == 1 and _right_limit is not None:
            for _x in range(_new_spring_points[0][0], _right_limit + 1):
                _water.add((_x, _pos[1]))
            break
        elif len(_new_spring_points) == 1 and _right_limit is None and _left_limit is None:
            return []
        else:
            break

    return _new_spring_points


clay = set()
water = set()
min_y = float('inf')
max_y = -float('inf')
min_x = 500
max_x = 500
for line in puzzle:
    x_match = re.search(r"x=(\d+)(?:\.\.(\d+))?", line)
    y_match = re.search(r"y=(\d+)(?:\.\.(\d+))?", line)

    if x_match.group(2) is None:
        x = int(x_match[1])
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        start_y = int(y_match[1])
        if start_y < min_y:
            min_y = start_y
        end_y = int(y_match[2])
        if end_y > max_y:
            max_y = end_y
        for y in range(start_y, end_y + 1):
            clay.add((x, y))
    elif y_match.group(2) is None:
        y = int(y_match[1])
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        start_x = int(x_match[1])
        if start_x < min_x:
            min_x = start_x
        end_x = int(x_match[2])
        if end_x > max_x:
            max_x = end_x
        for x in range(start_x, end_x + 1):
            clay.add((x, y))
    else:
        print(f'Find invalid line: {line}')
        exit(1)

spring_points = {(500, min_y - 1)}
while len(spring_points) > 0:
    spring_point = spring_points.pop()
    spring_points = spring_points.union(water_fall(spring_point, clay, water, max_y))

output_part_1 = len(water)
expected_output_part_1 = 38409
if output_part_1 == expected_output_part_1:
    print(f"✅ Challenge Part 1 -> {output_part_1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part_1}, got {output_part_1}")

output_part_2 = len(water.intersection(clay))
expected_output_part_2 = 32288
if output_part_2 == expected_output_part_2:
    print(f"✅ Challenge Part 2 -> {output_part_2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part_2}, got {output_part_2}")
