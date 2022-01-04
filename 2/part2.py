#!/usr/bin/env python3

import sys

def main():
    moves = []
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            line = line.rstrip().split()
            moves.append((line[0], int(line[1])))

    pos = [0, 0]
    aim = 0
    for direction, amount in moves:
        if direction == 'forward':
            pos[0] += amount
            pos[1] += amount * aim
        elif direction == 'up':
            aim -= amount
        elif direction == 'down':
            aim += amount

    print(f'{pos=}\nproduct={pos[0]*pos[1]}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part2 <inputfile>')
    main()
