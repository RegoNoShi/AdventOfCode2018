
import re

puzzle = open("../inputs/Day7.txt", "r").readlines()

required_for = {}
depends_on = {}
all_steps = set()
for line in puzzle:
    match = re.search(r"Step (\w) must be finished before step (\w) can begin\.", line)
    before = match.group(1)
    after = match.group(2)
    if before in required_for:
        required_for[before].add(after)
    else:
        required_for[before] = set(after)
    if after in depends_on:
        depends_on[after].add(before)
    else:
        depends_on[after] = set(before)
    all_steps.add(before)
    all_steps.add(after)


def is_ready(_step):
    if _step in depends_on:
        return len(depends_on[_step].difference(completed_steps)) == 0
    else:
        return True


available_steps = sorted(all_steps.difference(depends_on.keys()))

solution = ''
completed_steps = set()

while len(available_steps) > 0:
    step = available_steps.pop(0)

    if step not in completed_steps:
        solution += step
        completed_steps.add(step)

        if step in required_for:
            for next_step in required_for[step]:
                if is_ready(next_step):
                    available_steps.append(next_step)
        available_steps.sort()


output_part1 = solution
expected_output_part1 = 'FMOXCDGJRAUIHKNYZTESWLPBQV'
if output_part1 == expected_output_part1:
    print(f"✅ Challenge Part 1 -> {output_part1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part1}, got {output_part1}")


def available(_step, _required_for):
    for _, required_steps in _required_for.items():
        if _step in required_steps:
            return False
    return True


def first_available_worker(_workers):
    ws = [w for w in _workers if w[1] is None]
    return ws[0] if len(ws) > 0 else None


def first_done_worker(_workers):
    ws = [w for w in _workers if w[1] is not None]
    return min(ws, key=lambda w: w[2]) if len(ws) > 0 else None


completed_steps = set()
next_steps = all_steps.difference(depends_on.keys())
time = 0
workers = [(i, None, 0) for i in range(5)]
delay = 60
worker = None
while len(required_for) > 0:
    available_steps = [step for step in next_steps if available(step, required_for)]
    worker = first_available_worker(workers)

    while worker is None or len(available_steps) == 0:
        to_complete = first_done_worker(workers)
        if to_complete[1] in required_for:
            next_steps = next_steps.union(set(required_for[to_complete[1]]))
            del required_for[to_complete[1]]
        time = to_complete[2]
        completed_steps.add(to_complete[1])
        for step in [s for s in completed_steps if s in next_steps]:
            next_steps.remove(step)
        workers[to_complete[0]] = (to_complete[0], None, 0)

        available_steps = [step for step in next_steps if available(step, required_for)]
        worker = first_available_worker(workers)

    step = min(available_steps)
    workers[worker[0]] = (worker[0], step, time + delay + ord(step) - 64)
    next_steps.remove(step)

expected_output_part2 = 1053
output_part2 = workers[worker[0]][2]
if output_part2 == expected_output_part2:
    print(f"✅ Challenge Part 1 -> {output_part2}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part2}, got {output_part2}")
