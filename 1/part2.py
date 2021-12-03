#!/usr/bin/python3

import sys

def main():
    nums = []
    with open(sys.argv[1]) as f:
        nums = [int(n.rstrip()) for n in f.readlines()]

    windows = [nums[i-1:i+2] for i in range(1, len(nums)-1)]
    sums = [sum(w) for w in windows]

    increases = 0
    for i in range(1, len(sums)):
        if sums[i] > sums[i-1]:
            increases += 1

    print(f'{increases=}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: ./part2.py <inputfile>")
    main()
