#!/usr/bin/env python3

import sys

def main():
    grid = []
    with open(sys.argv[1]) as f:
        grid = [[int(n) for n in l.rstrip()] for l in f.readlines()]
    w, h = len(grid), len(grid[0])

    for step in range(1000):
        for i in range(h):
            for j in range(w):
                grid[i][j] += 1

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

        for i, j in flashed:
            grid[i][j] = 0

        for i in range(h):
            for j in range(w):
                print(grid[i][j], end='')
            print()
        print()

        if len(flashed) == w * h:
            print(f'{step+1=}')
            return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part2.py <file>')
    main()
