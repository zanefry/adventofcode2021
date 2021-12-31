#!/usr/bin/env python3

import sys

# It would be faster to update the counts concurrently with a map
# I'll try to figure that out later

def main():
# version A
#    zeros = 12*[0]
#    ones = 12*[0]
#
#    with open(sys.argv[1]) as f:
#        for line in f.readlines():
#            line = line.rstrip()
#            for i, c in enumerate(line):
#                if c == '0': zeros[i] += 1
#                else:        ones[i] += 1

#    for i in range(12):
#        if zeros[i] <= ones[i]:
#            gamma += '1'
#            epsilon += '0'
#        else:
#            gamma += '0'
#            epsilon += '1'
#
#    print(f'{gamma=} {epsilon=}')
#    print(f'product={int(gamma, 2) * int(epsilon, 2)}')

# version B
    bin_strings = []
    with open(sys.argv[1]) as f:
        bin_strings = [s.rstrip() for s in f.readlines()]

    columns = [[s[i] for s in bin_strings] for i in range(12)]
    counts = [c.count('1') for c in columns]

    gamma = ''.join(['1' if n >= 500 else '0' for n in counts])
    epsilon = ''.join(['1' if c == '0' else '0' for c in gamma])
    gamma, epsilon  = int(gamma, 2), int(epsilon, 2)

    print(f'{gamma=} {epsilon=}')
    print(gamma * epsilon)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part1 <inputfile>')
    main()
