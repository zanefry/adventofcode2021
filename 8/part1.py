#!/usr/bin/env python3

# for part 1 it wasn't actually necessary to do the decoding

import sys

def main():
    lines = []
    with open(sys.argv[1]) as f:
        lines = [l.rstrip().split(' | ') for l in f.readlines()]
    hints = [l[0].split() for l in lines]
    ciphertexts = [l[1].split() for l in lines]

    whole_ciphertext = []
    for c in ciphertexts:
        whole_ciphertext.extend(c)

    num_1s = len([d for d in whole_ciphertext if len(d) == 2])
    num_4s = len([d for d in whole_ciphertext if len(d) == 4])
    num_7s = len([d for d in whole_ciphertext if len(d) == 3])
    num_8s = len([d for d in whole_ciphertext if len(d) == 7])

    print(num_1s + num_4s + num_7s + num_8s)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part1.py <inputfile>')
    main()
