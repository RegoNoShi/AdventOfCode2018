
def print_field(_field):
    for _r in xrange(len(_field)):
        print ''.join(_field[_r][:-1])


puzzle = open("Day13.txt", "r").readlines()
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
for row in xrange(len(puzzle)):
    puzzle[row] = list(puzzle[row])
    for col in xrange(len(puzzle[row])):
        if puzzle[row][col] in directions:
            cart[(row, col)] = (puzzle[row][col], 'L', directions[puzzle[row][col]])

incident = False
while len(cart) > 1:
    for pos in sorted(cart.iterkeys()):
        if pos not in cart:
            continue
        status = cart[pos]
        if status[0] == '>':
            next_pos = (pos[0], pos[1] + 1)
        elif status[0] == '<':
            next_pos = (pos[0], pos[1] - 1)
        elif status[0] == 'v':
            next_pos = (pos[0] + 1, pos[1])
        else:
            next_pos = (pos[0] - 1, pos[1])

        next_cell = puzzle[next_pos[0]][next_pos[1]]

        if next_cell in directions:
            print '--- Incident:', next_pos, '---'
            puzzle[pos[0]][pos[1]] = status[2]
            status_cart_2 = cart[next_pos]
            puzzle[next_pos[0]][next_pos[1]] = status_cart_2[2]
            del cart[pos]
            del cart[next_pos]
            continue
        elif next_cell != '+':
            next_direction = directions_update[(status[0], next_cell)]
            next_turn = status[1]
        else:
            next_direction = directions_update[(status[0], status[1])]
            next_turn = turn_updates[status[1]]

        if next_direction == '#':
            print '### Fatal error:', pos, status, next_pos, next_cell, next_direction, '###'

        puzzle[pos[0]][pos[1]] = status[2]
        puzzle[next_pos[0]][next_pos[1]] = next_direction
        del cart[pos]
        cart[next_pos] = (next_direction, next_turn, next_cell)

        # print pos, status, next_pos, next_cell, next_direction, (next_direction, next_turn, next_cell)
    # print_field(puzzle)
print cart