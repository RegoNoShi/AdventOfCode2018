
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


def is_ready(_step, _depends_on, _completed_steps):
    if _step in _depends_on:
        return len(_depends_on[_step].difference(_completed_steps)) == 0
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
                if is_ready(next_step, depends_on, completed_steps):
                    available_steps.append(next_step)
        available_steps.sort()


output_part1 = solution
expected_output_part1 = 'FMOXCDGJRAUIHKNYZTESWLPBQV'
if output_part1 == expected_output_part1:
    print(f"✅ Challenge Part 1 -> {output_part1}")
else:
    print(f"❌ Challenge Part 1 -> Expected output {expected_output_part1}, got {output_part1}")


available_steps = sorted(all_steps.difference(depends_on.keys()))
completed_steps = set()
workers = [('', -1) for _ in range(5)]
time = 0


def pending_workers(_workers):
    for _worker in _workers:
        if _worker[0] != '':
            return True
    return False


def first_available_worker(_workers):
    for index in range(len(_workers)):
        if _workers[index][0] == '':
            return index
    return None


def next_step(_available_steps):
    if len(_available_steps) > 0:
        return _available_steps[0]
    return None


def next_completed_step(_workers):
    min_time = float('inf')
    min_worker = None
    for index in range(len(_workers)):
        if _workers[index][0] != '':
            if _workers[index][1] < min_time:
                min_time = _workers[index][1]
                min_worker = index
    return min_worker


while len(available_steps) > 0 or pending_workers(workers):
    worker = first_available_worker(workers)
    step = next_step(available_steps)

    if worker is not None and step is not None:
        workers[worker] = (step, time + ord(step) - 4)
        available_steps.remove(step)
    else:
        worker_id = next_completed_step(workers)
        completed_step, time = workers[worker_id]
        workers[worker_id] = ('', -1)
        completed_steps.add(completed_step)
        if completed_step in required_for:
            for new_step in required_for[completed_step]:
                if new_step in depends_on and len(depends_on[new_step].difference(completed_steps)) == 0:
                    available_steps.append(new_step)
            available_steps.sort()

expected_output_part2 = 1053
output_part2 = time
if output_part2 == expected_output_part2:
    print(f"✅ Challenge Part 2 -> {output_part2}")
else:
    print(f"❌ Challenge Part 2 -> Expected output {expected_output_part2}, got {output_part2}")
