#!/usr/bin/env python3

import sys

def main():
    grid = []
    with open(sys.argv[1]) as f:
        grid = [[int(n) for n in l.rstrip()] for l in f.readlines()]
    w, h = len(grid), len(grid[0])

    total_flashes = 0
    for _ in range(100):
        for i in range(h):
            for j in range(w):
                print(0 if grid[i][j] == 0 else '+', end='')
                grid[i][j] += 1
            print()
        print()

        flashed = set()
        new_flash = True
        while(new_flash):
            new_flash = False
            for i in range(h):
                for j in range(w):
                    if grid[i][j] > 9 and (i, j) not in flashed:
                        new_flash = True
                        flashed.add((i, j))

                        x, y = [0], [0]
                        if i != 0: y.append(-1)
                        if j != 0: x.append(-1)
                        if i != h-1: y.append(1)
                        if j != w-1: x.append(1)

                        for dy in y:
                            for dx in x:
                                if dy != 0 or dx != 0:
                                    grid[i+dy][j+dx] += 1

        total_flashes += len(flashed)
        for i, j in flashed:
            grid[i][j] = 0

    print(f'{total_flashes=}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part1.py <file>')
    main()
