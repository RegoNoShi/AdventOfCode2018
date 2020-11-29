
import re, sys
from math import pow


def move(_points, _speeds):
    return [(_points[idx][0] + _speeds[idx][0], _points[idx][1] + _speeds[idx][1]) for idx in xrange(len(_points))]


def draw(_points):
    field = ''
    for _y in xrange(min([p[1] for p in _points]), max([p[1] for p in _points]) + 1):
        for _x in xrange(min([p[0] for p in _points]), max([p[0] for p in _points]) + 1):
            if (_x, _y) in _points:
                field += '# '
            else:
                field += '. '
        field += '\n'
    print field


puzzle = open("Day10.txt", "r").readlines()
# puzzle = ["position=< 9,  1> velocity=< 0,  2>", "position=< 7,  0> velocity=<-1,  0>",
#           "position=< 3, -2> velocity=<-1,  1>", "position=< 6, 10> velocity=<-2, -1>",
#           "position=< 2, -4> velocity=< 2,  2>", "position=<-6, 10> velocity=< 2, -2>",
#           "position=< 1,  8> velocity=< 1, -1>", "position=< 1,  7> velocity=< 1,  0>",
#           "position=<-3, 11> velocity=< 1, -2>", "position=< 7,  6> velocity=<-1, -1>",
#           "position=<-2,  3> velocity=< 1,  0>", "position=<-4,  3> velocity=< 2,  0>",
#           "position=<10, -3> velocity=<-1,  1>", "position=< 5, 11> velocity=< 1, -2>",
#           "position=< 4,  7> velocity=< 0, -1>", "position=< 8, -2> velocity=< 0,  1>",
#           "position=<15,  0> velocity=<-2,  0>", "position=< 1,  6> velocity=< 1,  0>",
#           "position=< 8,  9> velocity=< 0, -1>", "position=< 3,  3> velocity=<-1,  1>",
#           "position=< 0,  5> velocity=< 0, -1>", "position=<-2,  2> velocity=< 2,  0>",
#           "position=< 5, -2> velocity=< 1,  2>", "position=< 1,  4> velocity=< 2,  1>",
#           "position=<-2,  7> velocity=< 2, -2>", "position=< 3,  6> velocity=<-1, -1>",
#           "position=< 5,  0> velocity=< 1,  0>", "position=<-6,  0> velocity=< 2,  0>",
#           "position=< 5,  9> velocity=< 1, -2>", "position=<14,  7> velocity=<-2,  0>",
#           "position=<-3,  6> velocity=< 2, -1>"]

points = []
speeds = []
avg_d = 0
for line in puzzle:
    match = re.search("position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>", line)
    x, y, dx, dy = [int(match.group(i)) for i in xrange(1, 5)]
    points.append((x, y))
    speeds.append((dx, dy))

min_height = sys.maxint
time = 0
while True:
    new_points = move(points, speeds)
    height = max([p[1] for p in new_points]) - abs(min([p[1] for p in new_points]))
    if height > min_height:
        draw(points)
        print time
        break
    time += 1
    min_height = height
    points = new_points
