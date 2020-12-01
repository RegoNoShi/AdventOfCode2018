
def print_field(_field):
    for _r in range(len(_field)):
        print(''.join(_field[_r][:-1]))


puzzle = [list(line) for line in open("../inputs/Day13.txt", "r").readlines()]
# puzzle = open("Day13.txt", "r").readlines()
# puzzle = ['/->-\        ',
#           '|   |  /----\\',
#           '| /-+--+-\  |',
#           '| | |  | v  |',
#           '\-+-/  \-+--/',
#           '  \------/   ']

cart = {}
directions = {'>': '-', '<': '-', '^': '|', 'v': '|'}
turn_updates = {'L': 'S', 'S': 'R', 'R': 'L'}
directions_update = {('>', '-'): '>', ('<', '-'): '<', ('v', '|'): 'v', ('^', '|'): '^',
                     ('>', '/'): '^', ('>', '\\'): 'v', ('<', '/'): 'v', ('<', '\\'): '^',
                     ('v', '/'): '<', ('v', '\\'): '>', ('^', '/'): '>', ('^', '\\'): '<',
                     ('v', '-'): '#', ('^', '-'): '#', ('<', '|'): '#', ('>', '|'): '#',
                     ('v', 'L'): '>', ('v', 'R'): '<', ('v', 'S'): 'v',
                     ('^', 'L'): '<', ('^', 'R'): '>', ('^', 'S'): '^',
                     ('<', 'L'): 'v', ('<', 'R'): '^', ('<', 'S'): '<',
                     ('>', 'L'): '^', ('>', 'R'): 'v', ('>', 'S'): '>'}

for row in range(len(puzzle)):
    for col in range(len(puzzle[row])):
        if puzzle[row][col] in directions:
            cart[(col, row)] = (puzzle[row][col], 'L', directions[puzzle[row][col]])

first_crash = (-1, -1)
incident = False
while len(cart) > 1:
    for pos in sorted(cart.keys()):
        if pos not in cart:
            continue
        status = cart[pos]
        if status[0] == '>':
            next_pos = (pos[0] + 1, pos[1])
        elif status[0] == '<':
            next_pos = (pos[0] - 1, pos[1])
        elif status[0] == 'v':
            next_pos = (pos[0], pos[1] + 1)
        else:
            next_pos = (pos[0], pos[1] - 1)

        next_cell = puzzle[next_pos[1]][next_pos[0]]

        if next_cell in directions:
            if first_crash == (-1, -1):
                first_crash = next_pos
            puzzle[pos[1]][pos[0]] = status[2]
            status_cart_2 = cart[next_pos]
            puzzle[next_pos[1]][next_pos[0]] = status_cart_2[2]
            del cart[pos]
            del cart[next_pos]
            continue
        elif next_cell != '+':
            next_direction = directions_update[(status[0], next_cell)]
            next_turn = status[1]
        else:
            next_direction = directions_update[(status[0], status[1])]
            next_turn = turn_updates[status[1]]

        puzzle[pos[1]][pos[0]] = status[2]
        puzzle[next_pos[1]][next_pos[0]] = next_direction
        del cart[pos]
        cart[next_pos] = (next_direction, next_turn, next_cell)

output_part_1 = first_crash
expected_output_part_1 = (26, 99)
if output_part_1 == expected_output_part_1:
    print(f"✅ Challenge Part 1 -> {output_part_1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part_1}, got {output_part_1}")

output_part_2 = list(cart.keys())[0]
expected_output_part_2 = (62, 48)
if output_part_2 == expected_output_part_2:
    print(f"✅ Challenge Part 2 -> {output_part_2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part_2}, got {output_part_2}")
