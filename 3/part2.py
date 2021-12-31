#!/usr/bin/env python3

import sys

def main():
    bin_strings = []
    with open(sys.argv[1]) as f:
        bin_strings = [s.rstrip() for s in f.readlines()]

    # most common filter
    pool = bin_strings.copy()
    for i in range(12):
        num_ones = [s[i] for s in pool].count('1')
        if num_ones >= len(pool) - num_ones:
            most_common = '1'
        else:
            most_common = '0'

        pool = [s for s in pool if s[i] == most_common]
        if len(pool) == 1:
            break
    oxygen_generator_rating = int(pool[0], 2)

    # least common filter
    pool = bin_strings.copy()
    for i in range(12):
        num_ones = [s[i] for s in pool].count('1')
        if num_ones < len(pool) - num_ones:
            least_common = '1'
        else:
            least_common = '0'

        pool = [s for s in pool if s[i] == least_common]
        if len(pool) == 1:
            break
    co2_scrubber_rating = int(pool[0], 2)

    print(f'{oxygen_generator_rating=} {co2_scrubber_rating=}')
    print(oxygen_generator_rating * co2_scrubber_rating)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part2 <inputfile>')
    main()
