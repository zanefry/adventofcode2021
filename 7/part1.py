#!/usr/bin/env python3

import sys

def main():
    crab_positions = []
    with open(sys.argv[1]) as f:
        crab_positions = [int(n) for n in f.read().rstrip().split(',')]

    fuel_costs = [sum([abs(p - n) \
            for p in crab_positions]) \
            for n in range(max(crab_positions))]

    min_cost = min(fuel_costs)
    print(f'{min_cost} @ {fuel_costs.index(min_cost)}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part1.py <inputfile>')
    main()
