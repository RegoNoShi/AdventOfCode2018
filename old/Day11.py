
import sys


def power_level(_x, _y, _sn):
    return (((((_x + 10) * _y + _sn) * (_x + 10)) / 100) % 10) - 5


print power_level(3, 5, 8) == 4
print power_level(122, 79, 57) == -5
print power_level(217, 196, 39) == 0
print power_level(101, 153, 71) == 4

grid_serial_numbers = [5791]

for grid_serial_number in grid_serial_numbers:
    grid = [power_level(x, y, grid_serial_number) for x in xrange(1, 301) for y in xrange(1, 301)]

    max_fuel = -sys.maxint
    max_pos = None
    for grid_size in xrange(1, 301):
        for x in xrange(0, 301 - grid_size):
            for y in xrange(0, 301 - grid_size):
                fuel = sum([grid[xx * 300 + yy] for xx in xrange(x, x + grid_size) for yy in xrange(y, y + grid_size)])
                if fuel > max_fuel:
                    max_fuel = fuel
                    max_pos = (x + 1, y + 1, grid_size)
                    print grid_serial_number, max_fuel, max_pos
