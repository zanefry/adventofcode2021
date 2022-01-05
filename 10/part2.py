#!/usr/bin/env python3

import sys

def main():
    lines = set()
    with open(sys.argv[1]) as f:
        lines = set([l.rstrip() for l in f.readlines()])

    corrupted = set()
    stack = []
    for line in lines:
        for c in line:
            if c in '([{<':
                stack.append(c)
            elif ')]}>'.index(c) != '([{<'.index(stack[-1]):
                corrupted.add(line)
                break
            else:
                stack.pop()

    incomplete = lines - corrupted

    scores = []
    for line in incomplete:
        score = 0
        stack = []
        for c in line:
            if c in '([{<': stack.append(c)
            else: stack.pop()

        for c in reversed(stack):
            score *= 5
            score += '([{<'.index(c) + 1

        scores.append(score)
    print(sorted(scores)[len(scores) // 2])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part2.py <file>')
    main()
