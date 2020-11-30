
import re


def line_to_event(_line):
    base_regex = r"\[\d+-\d+-\d+\s\d+:(\d+)\]\s"
    match = re.search(base_regex + r"wakes\sup", _line)
    if match is not None:
        return "w", int(match.group(1)), None
    match = re.search(base_regex + r"falls\sasleep", _line)
    if match is not None:
        return "a", int(match.group(1)), None
    match = re.search(base_regex + r"Guard\s#(\d+)\sbegins\sshift", _line)
    if match is not None:
        return "s", int(match.group(1)), int(match.group(2))


puzzle = sorted(map(lambda box_id: box_id, open("../inputs/Day4.txt", "r").readlines()))

guards = {}
most_asleep_guard = None
most_asleep_time = 0
most_times_asleep = 0
most_times_asleep_minute = None
most_times_asleep_guard = None
curr_guard = ""
start_asleep = -1

for line in puzzle:
    op, minute, guard = line_to_event(line)
    if op == "s":
        curr_guard = guard
    elif op == "a":
        start_asleep = minute
    elif op == "w":
        if curr_guard in guards:
            guards[curr_guard]["total"] += minute - start_asleep
        else:
            guards[curr_guard] = {}
            guards[curr_guard]["total"] = minute - start_asleep
        for m in range(start_asleep, minute):
            if m in guards[curr_guard]:
                guards[curr_guard][m] += 1
            else:
                guards[curr_guard][m] = 1
            if guards[curr_guard][m] > most_times_asleep:
                most_times_asleep = guards[curr_guard][m]
                most_times_asleep_guard = curr_guard
                most_times_asleep_minute = m

        if guards[curr_guard]["total"] > most_asleep_time:
            most_asleep_time = guards[curr_guard]["total"]
            most_asleep_guard = curr_guard

most_asleep_minute = None
most_asleep_minute_times = 0
for minute, times in guards[most_asleep_guard].items():
    if minute != "total" and times > most_asleep_minute_times:
        most_asleep_minute_times = times
        most_asleep_minute = minute

expected_output_part1 = 26281
output_part1 = most_asleep_guard * most_asleep_minute
if output_part1 == expected_output_part1:
    print(f"✅ Challenge Part 1 -> {output_part1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part1}, got {output_part1}")

expected_output_part2 = 73001
output_part2 = most_times_asleep_guard * most_times_asleep_minute
if output_part2 == expected_output_part2:
    print(f"✅ Challenge Part 2 -> {output_part2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output '{expected_output_part2}', got '{output_part2}'")
