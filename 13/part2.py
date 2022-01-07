#!/usr/bin/env python3

import sys

def fold_up(p: tuple[int, int], line: int) -> tuple[int, int]:
    x, y = p
    return (x, line - (y - line))

def fold_left(p: tuple[int, int], line: int) -> tuple[int, int]:
    x, y = p
    return (line - (x - line), y)

def main():
    points = set()
    folds = []
    with open(sys.argv[1]) as f:
        parts = f.read().split('\n\n')

        for line in parts[0].split('\n'):
            points.add(tuple([int(n) for n in line.split(',')]))
        for line in parts[1].rstrip().split('\n'):
            fold = line.split()[-1].split('=')
            fold = fold[0], int(fold[1])
            folds.append(fold)

    for fold in folds:
        axis, line = fold
        if axis == 'x':
            affected = [(x, y) for x, y in points if x > line]
            points.update(set([fold_left(p, line) for p in affected]))
        else:
            affected = [(x, y) for x, y in points if y > line]
            points.update(set([fold_up(p, line) for p in affected]))
        points -= set(affected)

    for y in range(max([y for _, y in points]) + 1):
        for x in range(max([x for x, _ in points]) + 1):
            print('#' if (x, y) in points else ' ', end='')
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part2.py <file>')
    main()
