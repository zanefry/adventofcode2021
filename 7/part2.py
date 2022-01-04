#!/usr/bin/env python3

# The new cost that goes 2 -> 1+2, 3 -> 1+2+3, ... is a function I know,
# usually called T(n) and sequence is called the triangular numbers
# To avoid computing the sum we can use the formula T(n) = (n*(n+1))/2

import sys

def main():
    crab_positions = []
    with open(sys.argv[1]) as f:
        crab_positions = [int(n) for n in f.read().rstrip().split(',')]

    fuel_costs = [sum([(abs(p-n)*(abs(p-n)+1))/2 \
            for p in crab_positions]) \
            for n in range(max(crab_positions))]

    min_cost = min(fuel_costs)
    print(f'{min_cost} @ {fuel_costs.index(min_cost)}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part2.py <inputfile>')
    main()
