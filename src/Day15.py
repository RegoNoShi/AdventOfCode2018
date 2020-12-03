
puzzle = [list(line.strip()) for line in open("../inputs/Day15.txt", "r").readlines()]


def find_best_move(_pos, _targets, _allies, _cavern):
    if len(_targets) == 0:
        return None

    if _pos not in _allies:
        return None

    _available_steps = []
    for _offset in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        _curr_pos = (_pos[0] + _offset[0], _pos[1] + _offset[1])
        if _curr_pos in _targets:
            return None
        if _curr_pos in _cavern and _curr_pos not in _allies:
            _available_steps.append((_curr_pos, 1, _curr_pos))
    if len(_available_steps) == 0:
        return None

    _target_positions = []
    for _target in _targets:
        for _offset in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            _target_pos = (_target[0] + _offset[0], _target[1] + _offset[1])
            if _target_pos in _cavern and _target_pos not in _allies and _target_pos not in _targets:
                _target_positions.append(_target_pos)
    if len(_target_positions) == 0:
        return None

    _visited = set()
    _best_position = None
    _min_distance = None
    _best_first_step = None
    while len(_available_steps) > 0:
        _curr_pos, _curr_distance, _curr_first_step = _available_steps.pop(0)

        if _min_distance is not None and _curr_distance > _min_distance:
            break

        if _curr_pos in _visited:
            continue
        _visited.add(_curr_pos)

        if _curr_pos in _target_positions:
            if _best_position is None or _best_first_step is None or _min_distance is None:
                _min_distance = _curr_distance
                _best_position = _curr_pos
                _best_first_step = _curr_first_step
            elif _curr_distance < _min_distance or (_curr_distance == _min_distance and (_curr_pos < _best_position)) or \
                    (_curr_distance == _min_distance and _curr_pos == _best_position and _curr_first_step < _best_first_step):
                _min_distance = _curr_distance
                _best_position = _curr_pos
                _best_first_step = _curr_first_step

        for _offset in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            _next_pos = (_curr_pos[0] + _offset[0], _curr_pos[1] + _offset[1])
            if _next_pos in _cavern and _next_pos not in _targets and _next_pos not in _allies:
                _available_steps.append((_next_pos, _curr_distance + 1, _curr_first_step))

    return _best_first_step


def find_best_attack(_pos, _targets):
    if len(_targets) == 0:
        return None

    _min_points = None
    _best_target = None
    for _offset in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        _curr_pos = (_pos[0] + _offset[0], _pos[1] + _offset[1])
        if _curr_pos in _targets:
            if _min_points is None or _best_target is None:
                _min_points = _targets[_curr_pos]
                _best_target = _curr_pos
            elif _targets[_curr_pos] < _min_points:
                _min_points = _targets[_curr_pos]
                _best_target = _curr_pos
            elif _targets[_curr_pos] == _min_points and _curr_pos < _best_target:
                _min_points = _targets[_curr_pos]
                _best_target = _curr_pos

    return _best_target


def solve(_puzzle, elves_attack=3):
    sizes = (len(_puzzle), len(_puzzle[0]))
    cavern = set()
    goblins = {}
    elves = {}
    for x in range(sizes[0]):
        for y in range(sizes[1]):
            if _puzzle[x][y] in ['.', 'G', 'E']:
                cavern.add((x, y))
            if _puzzle[x][y] == 'G':
                goblins[(x, y)] = 200
            elif _puzzle[x][y] == 'E':
                elves[(x, y)] = 200

    death_elves = 0
    completed_combat_round = 0
    while len(elves) > 0 and len(goblins) > 0:
        move_order = sorted(list(elves.keys()) + list(goblins.keys()))

        while len(move_order) > 0:
            start_position = move_order.pop(0)
            targets, allies = (goblins, elves) if start_position in elves else (elves, goblins)

            if start_position not in allies:
                continue

            best_move = find_best_move(start_position, targets, allies, cavern)

            current_position = start_position
            if best_move is not None:
                player = allies.pop(start_position)
                allies[best_move] = player
                current_position = best_move

            best_target = find_best_attack(current_position, targets)

            if best_target is not None:
                if best_target in goblins:
                    if targets[best_target] <= elves_attack:
                        if best_target in move_order:
                            move_order.remove(best_target)
                        del targets[best_target]
                    else:
                        targets[best_target] -= elves_attack
                else:
                    if targets[best_target] <= 3:
                        if best_target in move_order:
                            move_order.remove(best_target)
                        del targets[best_target]
                        death_elves += 1
                    else:
                        targets[best_target] -= 3
            if len(targets) == 0 and len(move_order) > 0:
                break
        else:
            completed_combat_round += 1
    return completed_combat_round * sum([goblins[p] for p in goblins] + [elves[p] for p in elves]), death_elves


def solve_part2(_puzzle):
    elves_attack = 4
    while True:
        score, death_elves = solve(_puzzle, elves_attack)
        if death_elves == 0:
            return score
        elves_attack += 1


output_part_1, _ = solve(puzzle)
expected_output_part_1 = 228730
if output_part_1 == expected_output_part_1:
    print(f"✅ Challenge Part 1 -> {output_part_1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part_1}, got {output_part_1}")

output_part_2 = solve_part2(puzzle)
expected_output_part_2 = 33621
if output_part_2 == expected_output_part_2:
    print(f"✅ Challenge Part 2 -> {output_part_2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part_2}, got {output_part_2}")
