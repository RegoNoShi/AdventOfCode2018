
import re

puzzle = open("Day7.txt", "r").readlines()

# puzzle = ["Step C must be finished before step A can begin.", "Step C must be finished before step F can begin.",
#           "Step A must be finished before step B can begin.", "Step A must be finished before step D can begin.",
#           "Step B must be finished before step E can begin.", "Step D must be finished before step E can begin.",
#           "Step F must be finished before step E can begin."]


def available(step, graph):
    for _, nexts in graph.iteritems():
        if step in nexts:
            return False
    return True


def first_available_worker(workers):
    ws = [w for w in workers if w[1] is None]
    return ws[0] if len(ws) > 0 else None


def first_done_worker(workers):
    ws = [w for w in workers if w[1] is not None]
    return min(ws, key=lambda w: w[2]) if len(ws) > 0 else None


graph = {}
all_before = set()
all_after = set()
for line in puzzle:
    match = re.search("Step (\w) must be finished before step (\w) can begin\.", line)
    before = match.group(1)
    after = match.group(2)
    if before in graph:
        graph[before].append(after)
    else:
        graph[before] = [after]
    all_before.add(before)
    all_after.add(after)

solution = ''
next_steps = all_before.difference(all_after)
time = 0
workers = [(i, None, 0) for i in xrange(5)]
delay = 60

while len(graph) > 0:
    available_steps = [step for step in next_steps if available(step, graph)]
    worker = first_available_worker(workers)

    while worker is None or len(available_steps) == 0:
        to_complete = first_done_worker(workers)
        if to_complete[1] in graph:
            next_steps = next_steps.union(set(graph[to_complete[1]]))
            del graph[to_complete[1]]
        time = to_complete[2]
        solution += to_complete[1]
        for step in [s for s in solution if s in next_steps]:
            next_steps.remove(step)
        workers[to_complete[0]] = (to_complete[0], None, 0)

        available_steps = [step for step in next_steps if available(step, graph)]
        worker = first_available_worker(workers)

    step = min(available_steps)
    workers[worker[0]] = (worker[0], step, time + delay + ord(step) - 64)
    next_steps.remove(step)
print solution
print workers[worker[0]][2]
