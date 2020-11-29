
import re


def claim_to_size(claim):
    match = re.search("#\d+\s@\s(\d+),(\d+):\s(\d+)x(\d+)", claim)
    x = int(match.group(1))
    y = int(match.group(2))
    w = int(match.group(3))
    h = int(match.group(4))
    return x, y, w, h


def claim_overlap(occupied_spaces, x, y, w, h):
    for delta_x in range(w):
        for delta_y in range(h):
            if occupied_spaces[(x + delta_x, y + delta_y)] > 1:
                return True
    return False


occupied_spaces = {}


def insert_claim(x, y, w, h):
    for delta_x in range(w):
        for delta_y in range(h):
            if (x + delta_x, y + delta_y) in occupied_spaces:
                occupied_spaces[(x + delta_x, y + delta_y)] += 1
            else:
                occupied_spaces[(x + delta_x, y + delta_y)] = 1


puzzle = list(map(lambda box_id: box_id.strip(), open("../inputs/Day3.txt", "r").readlines()))

for claim in puzzle:
    insert_claim(*claim_to_size(claim))

expected_output_part1 = 121259
output_part1 = len([count for _, count in occupied_spaces.items() if count > 1])
if output_part1 == expected_output_part1:
    print(f"✅ Challenge -> {output_part1}")
else:
    print(f"❌ Challenge -> Expected output {expected_output_part1}, got {output_part1}")

expected_output_part2 = "#239 @ 851,350: 19x16"
output_part2 = None
for claim in puzzle:
    if not claim_overlap(occupied_spaces, *claim_to_size(claim)):
        output_part2 = claim
if output_part2 == expected_output_part2:
    print(f"✅ Challenge -> {output_part2}")
else:
    print(f"❌ Challenge -> Expected output '{expected_output_part2}', got '{output_part2}'")
