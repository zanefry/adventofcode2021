#!/usr/bin/env python3

import sys

nhbrs = {}
paths = set()

def dfs(v: str, visited: list[str], double: list[str]):
    global nbhrs
    global paths

    visited.append(v)

    if v == 'end':
        paths.add(tuple(visited))
        return

    for u in nhbrs[v]:
        if u.isupper() or u not in visited:
            dfs(u, visited.copy(), double)
        if (u not in visited and not double) or double == [u]:
            dfs(u, visited.copy(), double + [u])

def main():
    global neighbors
    with open(sys.argv[1]) as f:
        edges = [set(l.rstrip().split('-')) for l in f.readlines()]
        verts = set.union(*edges)

        for v in verts:
            nhbrs[v] = set.union(*[e for e in edges if v in e]) - {v}

    dfs('start', [], [])
    print(f'{len(paths)=}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part2.py <file>')
    main()
