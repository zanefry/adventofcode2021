#!/usr/bin/env python3

# To improve performance I'm switching from the simplest approach with a list of counters for each fish, to a list of fixed length 9 where the ith entry
# represents the number of fish counters currently on i. Then each day the 9 ints can be updated quickly

import sys

def main():
  fish_counters = []
  with open(sys.argv[1]) as f:
    fish_counters = [int(n) for n in f.read().rstrip().split(',')]

  totals = [fish_counters.count(n) for n in range(9)]

  for _ in range(256):
    times_up = totals[0]

    for i in range(8):
      totals[i] = totals[i+1]

    totals[8] = times_up
    totals[6] += times_up

  print(sum(totals))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    sys.exit('usage: ./part1.py <inputfile>')
  main()
