
import sys

puzzle = open("Day6.txt", "r").readlines()


def line_to_coord(idx, line):
    coord = line.split(", ")
    return int(coord[0]), int(coord[1]), idx


def min_distance(x, y, coords):
    min_dist = sys.maxint
    result = None
    total = 0
    for coord in coords:
        d = abs(x - coord[0]) + abs(y - coord[1])
        total += d
        if d < min_dist:
            min_dist = d
            result = coord[2]
        elif d == min_dist:
            result = -1
    return result, total


coords = map(lambda idx: line_to_coord(idx, puzzle[idx]), xrange(len(puzzle)))

max_x = max([x for x, _, _ in coords])
max_y = max([y for _, y, _ in coords])

field = [None] * max_x
counter = [0] * len(coords)
infinite = [False] * len(coords)
limit = 10000
less_than_limit = 0
for x in xrange(max_x):
    field[x] = [None] * max_y
    for y in xrange(max_y):
        (res, total) = min_distance(x, y, coords)
        if total < limit:
            less_than_limit += 1
        if res >= 0:
            field[x][y] = res
            counter[field[x][y]] += 1
            if x == 0 or y == 0 or x == (max_x - 1) or y == (max_y - 1):
                infinite[field[x][y]] = True

print(max([counter[idx] for idx in xrange(len(coords)) if infinite[idx] == False]))
print less_than_limit
