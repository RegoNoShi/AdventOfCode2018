
import re
from collections import deque, defaultdict


def max_score(_players, _marbles):
    field = deque([0])
    players_scores = defaultdict(int)

    for marble in range(1, _marbles + 1):
        if marble % 23 == 0:
            field.rotate(7)
            players_scores[marble % _players] += field.pop() + marble
            field.rotate(-1)
        else:
            field.rotate(-1)
            field.append(marble)

    return max(players_scores.values())


puzzle = open("../inputs/Day9.txt", "r").readline()

games = [(9, 25), (10, 1618), (13, 7999), (17, 1104), (21, 6111), (30, 5807)]
match = re.search(r"(\d+)\splayers;\slast\smarble\sis\sworth\s(\d+)\spoints", puzzle)
games.append((int(match.group(1)), int(match.group(2))))

top_score = 0
top_score_100_times = 0
for players, marbles in games:
    player_score = max_score(players, marbles)
    player_score_100_times = max_score(players, marbles * 100)
    if player_score > top_score:
        top_score = player_score
    if player_score_100_times > top_score_100_times:
        top_score_100_times = player_score_100_times

expected_output_part1 = 405143
output_part1 = top_score
if output_part1 == expected_output_part1:
    print(f"✅ Challenge Part 1 -> {output_part1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part1}, got {output_part1}")

expected_output_part2 = 3411514667
output_part2 = top_score_100_times
if output_part2 == expected_output_part2:
    print(f"✅ Challenge Part 2 -> {output_part2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part2}, got {output_part2}")

