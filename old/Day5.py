
puzzle = open("Day5.txt", "r").readline()

def react(polymer):
    reaction = True
    while reaction:
        reaction = False
        tmp_polymer = ""
        i = 0
        while i < xrange(len(polymer)):
            if i >= len(polymer):
                break
            if i == len(polymer) - 1:
                tmp_polymer += polymer[i]
                break
            if abs(ord(polymer[i]) - ord(polymer[i + 1])) != 32:
                tmp_polymer += polymer[i]
                i += 1
            else:
                i += 2
                reaction = True
        polymer = tmp_polymer
    return polymer

puzzle = react(puzzle)
print len(puzzle)

shortest_polymer = len(puzzle)
elements = set([c.lower() for c in puzzle])
for element in elements:
    tmp_puzzle = puzzle.replace(element, "")
    tmp_puzzle = tmp_puzzle.replace(element.upper(), "")
    tmp_puzzle = react(tmp_puzzle)
    if len(tmp_puzzle) < shortest_polymer:
        shortest_polymer = len(tmp_puzzle)
print shortest_polymer