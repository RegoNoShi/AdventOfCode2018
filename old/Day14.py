
puzzle = '047801'
scores = [3, 7]
pos = [0, 1]
int_puzzle = int(puzzle)
array_puzzle = [int(c) for c in puzzle]
part_1_complete = False
part_2_complete = False

while not (part_1_complete and part_2_complete):
    new_score = scores[pos[0]] + scores[pos[1]]
    if new_score >= 10:
        scores.append(new_score / 10)
    scores.append(new_score % 10)
    pos = [(p + scores[p] + 1) % len(scores) for p in pos]
    if not part_1_complete and len(scores) >= int_puzzle + 10:
        print 'Part 1:', ''.join([str(n) for n in scores[int_puzzle:int_puzzle + 10]])
        part_1_complete = True
    if not part_2_complete and (
            (len(scores) >= len(puzzle) and array_puzzle == scores[-len(puzzle):]) or
            (new_score >= 10 and len(scores) > len(puzzle) and array_puzzle == scores[-(len(puzzle) + 1):-1])):
        print 'Part 2:', len(scores) - len(puzzle)
        part_2_complete = True
