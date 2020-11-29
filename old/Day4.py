
import re


def line_to_event(line):
    base_regex = "\[\d+-\d+-\d+\s\d+:(\d+)\]\s"
    match = re.search(base_regex + "wakes\sup", line)
    if match is not None:
        return "w", int(match.group(1)), None
    match = re.search(base_regex + "falls\sasleep", line)
    if match is not None:
        return "a", int(match.group(1)), None
    match = re.search(base_regex + "Guard\s#(\d+)\sbegins\sshift", line)
    if match is not None:
        return "s", int(match.group(1)), int(match.group(2))


puzzle = sorted(open("Day4.txt", "r").readlines())

guards = {}
most_asleep_guard = None
most_asleep_time = 0
most_times_asleep = 0
most_times_asleep_minute = None
most_times_asleep_guard = None

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
        for m in xrange(start_asleep, minute):
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
for minute, times in guards[most_asleep_guard].iteritems():
    if minute != "total" and times > most_asleep_minute_times:
        most_asleep_minute_times = times
        most_asleep_minute = minute

print most_asleep_guard, most_asleep_minute, most_asleep_guard * most_asleep_minute
print most_times_asleep_guard, most_times_asleep_minute, most_times_asleep_guard * most_times_asleep_minute