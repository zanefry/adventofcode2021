#!/usr/bin/env python3

import sys

grid = []
visited = set()

def dfs(point: tuple[int, int]):
    global grid
    global visited
    visited.add(point)

    i, j = point

    nbhd = []
    if i != 0:
        if (i-1, j) not in visited and grid[i-1][j] != 9:
            nbhd.append((i-1, j))
    if i != len(grid) - 1:
        if (i+1, j) not in visited and grid[i+1][j] != 9:
            nbhd.append((i+1, j))
    if j != 0:
        if (i, j-1) not in visited and grid[i][j-1] != 9:
            nbhd.append((i, j-1))
    if j != len(grid[0]) - 1:
        if (i, j+1) not in visited and grid[i][j+1] != 9:
            nbhd.append((i, j+1))

    for p in nbhd: dfs(p)

def main():
    global grid
    global visited

    with open(sys.argv[1]) as f:
        grid = [[int(n) for n in l.rstrip()] for l in f.readlines()]

    h, w = len(grid), len(grid[0])
    lowpoints = []
    for i in range(h):
        for j in range(w):
            if i == 0 or grid[i-1][j] > grid[i][j]:
                if i == h-1 or grid[i+1][j] > grid[i][j]:
                    if j == 0 or grid[i][j-1] > grid[i][j]:
                        if j == w-1 or grid[i][j+1] > grid[i][j]:
                            lowpoints.append((i, j))

    basin_sizes = []
    for p in lowpoints:
        visited = set()
        dfs(p)
        basin_sizes.append(len(visited))

    print(sorted(basin_sizes)[-3:])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part2.py input')
    main()
