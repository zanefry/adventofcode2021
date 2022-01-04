#!/usr/bin/env python3

import sys

def main():
    grid = []
    with open(sys.argv[1]) as f:
        grid = [[int(n) for n in l.rstrip()] for l in f.readlines()]

    h, w = len(grid), len(grid[0])
    risk = 0
    for i in range(h):
        for j in range(w):
            if i == 0 or grid[i-1][j] > grid[i][j]:
                if i == h-1 or grid[i+1][j] > grid[i][j]:
                    if j == 0 or grid[i][j-1] > grid[i][j]:
                        if j == w-1 or grid[i][j+1] > grid[i][j]:
                            risk += grid[i][j] + 1

    print(risk)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part1.py input')
    main()
