#!/usr/bin/python3

import sys

def main():
    moves = []
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            line = line.rstrip().split()
            moves.append((line[0], int(line[1])))

    pos = [0, 0]
    for direction, amount in moves:
        if direction == 'forward':
            pos[0] += amount
        elif direction == 'up':
            pos[1] -= amount
        elif direction == 'down':
            pos[1] += amount

    print(f'{pos=}\nproduct={pos[0]*pos[1]}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part1 <inputfile>')
    main()
