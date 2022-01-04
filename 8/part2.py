#!/usr/bin/env python3

# we can use the given 1, 4, and 7 to deduce the rest and get the final
# numbers without cracking which segment is which

import sys

def main():
    lines = []
    with open(sys.argv[1]) as f:
        lines = [l.rstrip().split(' | ') for l in f.readlines()]

    hints = [[set(d) for d in l[0].split()] for l in lines]
    ciphertexts = [[set(d) for d in l[1].split()] for l in lines]

    digits = 10 * [set()]
    total = 0

    for i in range(len(hints)):
        for d in hints[i]:
            if len(d) == 2:
                digits[1] = d
            elif len(d) == 3:
                digits[7] = d
            elif len(d) == 4:
                digits[4] = d

        for d in hints[i]:
            if len(d) == 5: # 2, 3, 5
                lil_arm = digits[4] - digits[1]
                if digits[1].issubset(d):
                    digits[3] = d
                elif d.intersection(lil_arm) == lil_arm:
                    digits[5] = d
                else:
                    digits[2] = d
            elif len(d) == 6: # 0, 6, 9
                if not digits[1].issubset(d):
                    digits[6] = d
                elif digits[4].issubset(d):
                    digits[9] = d
                else:
                    digits[0] = d
            elif len(d) == 7:
                digits[8] = d

        decoded_digits = []
        for d in ciphertexts[i]:
            decoded_digits.append(digits.index(d))

        total += int(''.join([str(d) for d in decoded_digits]))
    print(total)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part2.py <inputfile>')
    main()
