#!/usr/bin/python

import sys

def fill_line(p0: tuple[int, int], p1: tuple[int, int]) -> set[tuple[int, int]]:
  points = set([p0, p1])

  if p0[1] == p1[1]: # horizontal case
    if p0[0] > p1[0]:
      p0, p1 = p1, p0
    for x in range(p0[0] + 1, p1[0]):
      points.add((x, p0[1]))
  else:              # vertical case
    if p0[1] > p1[1]:
      p0, p1 = p1, p0
    for y in range(p0[1] + 1, p1[1]):
      points.add((p0[0], y))

  return points


def main():
  counts = {}
  pairs = []
  with open(sys.argv[1]) as f:
    pairs = [[p.split(',') \
              for p in l.rstrip().split(' -> ')] \
              for l in f.readlines()]
    pairs = [[(int(p[0]), int(p[1])) for p in l] for l in pairs]

  # only horizontal and vertical lines for part 1
  pairs = [p for p in pairs if p[0][0] == p[1][0] or p[0][1] == p[1][1]]

  for pair in pairs:
    for point in fill_line(pair[0], pair[1]):
      counts[point] = counts.get(point, 0) + 1

  print(len([n for n in counts.values() if n > 1]))


if __name__ == "__main__":
  if len(sys.argv) != 2:
    sys.exit('usage: ./part1.py <inputfile>')
  main()
