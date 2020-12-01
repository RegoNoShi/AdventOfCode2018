
puzzle = 5791
grid_size = 300


def power_level(_x, _y, _sn):
    return (((((_x + 10) * _y + _sn) * (_x + 10)) // 100) % 10) - 5


def max_power(_grid, _max_square_size):
    _calculated_results = {}
    _grid_size = len(_grid)
    _max_power = -float('inf')
    _max_coordinates = (0, 0, 0)
    for _square_size in range(1, _max_square_size + 1):
        for _x in range(_grid_size - _square_size + 1):
            for _y in range(_grid_size - _square_size + 1):
                if (_x, _y) in _calculated_results:
                    _power = _calculated_results[(_x, _y)]
                else:
                    _power = 0
                for _offset in range(_square_size):
                    _power += grid[_x + _offset][_y + _square_size - 1] + grid[_x + _square_size - 1][_y + _offset]
                _power -= grid[_x + _square_size - 1][_y + _square_size - 1]
                _calculated_results[(_x, _y)] = _power
                if _power > _max_power:
                    _max_power = _power
                    _max_coordinates = (_x + 1, _y + 1, _square_size)
    return _max_power, _max_coordinates


grid = [[power_level(x, y, puzzle) for y in range(1, grid_size + 1)] for x in range(1, grid_size + 1)]

_, coordinates = max_power(grid, 3)
expected_coordinates = (20, 68, 3)
if coordinates == expected_coordinates:
    print(f"✅ Challenge Part 1 -> {coordinates}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_coordinates}, got {coordinates}")

_, coordinates = max_power(grid, grid_size)
expected_coordinates = (231, 273, 16)
if coordinates == expected_coordinates:
    print(f"✅ Challenge Part 2 -> {coordinates}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_coordinates}, got {coordinates}")
