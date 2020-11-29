
def difference(box_id1, box_id2):
    return len(list(filter(lambda x: x[0] != x[1], zip(box_id1, box_id2))))


def common_letters(box_id1, box_id2):
    res = ""
    for i in range(len(box_id1)):
        if box_id1[i] == box_id2[i]:
            res += box_id1[i]
    return res


def find_box_id():
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            diff = difference(puzzle[i], puzzle[j])
            if diff == 1:
                return common_letters(puzzle[i], puzzle[j])


puzzle = list(map(lambda box_id: box_id.strip(), open("../inputs/Day2.txt", "r").readlines()))
twice = 0
three_times = 0

for boxId in puzzle:
    letter_count = dict()
    for letter in boxId:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    if len(list(filter(lambda x: x == 2, letter_count.values()))) > 0:
        twice += 1
    if len(list(filter(lambda x: x == 3, letter_count.values()))) > 0:
        three_times += 1

expected_output_part1 = 7533
output_part1 = twice * three_times
if output_part1 == expected_output_part1:
    print(f"✅ Challenge -> {output_part1}")
else:
    print(f"❌ Challenge -> Expected output {expected_output_part1}, got {output_part1}")

expected_output_part2 = "mphcuasvrnjzzkbgdtqeoylva"
output_part2 = find_box_id()
if output_part2 == expected_output_part2:
    print(f"✅ Challenge -> {output_part2}")
else:
    print(f"❌ Challenge -> Expected output '{expected_output_part2}', got '{output_part2}'")
