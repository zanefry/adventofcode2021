#!/usr/bin/env python3

start: str
rules: dict
with open('input') as f:
    start, lines = f.read().split('\n\n')
    lines = lines.split('\n')[:-1]

    rules = {}
    for line in lines:
        (l, r), new = line.rstrip().split(' -> ')
        d = rules.get(l, {})
        d[r] = new
        rules[l] = d


step_limit = 41

prev = start
for step in range(1, step_limit):
    print(step)

    curr = []
    for i in range(len(prev) - 1):
        curr.append(prev[i])
        if prev[i + 1] in rules[prev[i]]:
            curr.append(rules[prev[i]][prev[i + 1]])

    curr.append(prev[-1])
    prev = curr

end = prev
counts = {}
for c in end:
    counts[c] = counts.get(c, 0) + 1

sorted_counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}
least_common = list(sorted_counts)[0]
most_common = list(sorted_counts)[-1]

print(counts[most_common] - counts[least_common])
