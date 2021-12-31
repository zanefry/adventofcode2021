#!/usr/bin/env python3

import sys

def main():
    fish_counters = []
    with open(sys.argv[1]) as f:
        fish_counters = [int(n) for n in f.read().rstrip().split(',')]

    for _ in range(40):
        new_fish = 0
        for i, n in enumerate(fish_counters):
            if n == 0:
                fish_counters[i] = 6
                new_fish += 1
        else:
            fish_counters[i] -= 1

    for _ in range(new_fish):
        fish_counters.append(8)

    print(len(fish_counters))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part1.py <inputfile>')
    main()
