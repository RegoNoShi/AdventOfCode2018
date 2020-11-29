
import re

puzzle = open("Day12.txt", "r").readlines()
# puzzle = ['initial state: #..#.#..##......###...###', '...## => #', '..#.. => #', '.#... => #', '.#.#. => #',
#           '.#.## => #', '.##.. => #', '.#### => #', '#.#.# => #', '#.### => #', '##.#. => #',
#           '##.## => #', '###.. => #', '###.# => #', '####. => #']
match = re.search("initial state:\s([\.#]+)", puzzle[0])

input = match.group(1)
field = [idx for idx in xrange(len(input)) if input[idx] == '#']
rules = set()
for line in puzzle[1:]:
    match = re.search("([\.#]+)\s=>\s([\.#]{1})", line)
    if match.group(2) == '#':
        rules.add(tuple(1 if c == '#' else 0 for c in match.group(1)))


def plant(_idx, _field):
    check = tuple([1 if c in _field else 0 for c in xrange(_idx - 2, _idx + 3)])
    if check in rules:
        return idx


diff = None
for gen in xrange(50000000000):
    min_idx = min(field) - 5
    max_idx = max(field) + 5

    new_field = [plant(idx, field) for idx in xrange(min_idx, max_idx) if plant(idx, field) is not None]
    if diff == sum(new_field) - sum(field):
        break
    diff = sum(new_field) - sum(field)
    field = new_field

print sum(field) + (diff * (50000000000 - gen))
