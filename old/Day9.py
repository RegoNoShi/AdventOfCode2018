
import re
from collections import deque, defaultdict


def max_score(_players, _marbles):
    field = deque([0])
    players_scores = defaultdict(int)

    for marble in xrange(1, _marbles + 1):
        if marble % 23 == 0:
            field.rotate(7)
            players_scores[marble % _players] += field.pop() + marble
            field.rotate(-1)
        else:
            field.rotate(-1)
            field.append(marble)

    return max(players_scores.itervalues())


puzzle = open("Day9.txt", "r").readline()

games = [(9, 25), (10, 1618), (13, 7999), (17, 1104), (21, 6111), (30, 5807)]
match = re.search("(\d+)\splayers;\slast\smarble\sis\sworth\s(\d+)\spoints", puzzle)
games.append((int(match.group(1)), int(match.group(2))))

for players, marbles in games:
    print max_score(players, marbles), max_score(players, marbles * 100)
