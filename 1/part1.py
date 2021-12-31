#!/usr/bin/env python3

import sys

def main():
    nums = []
    with open(sys.argv[1]) as f:
        nums = [int(n.rstrip()) for n in f.readlines()]

    increases = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            increases += 1

    print(f'{increases=}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: ./part1.py <inputfile>")
    main()
