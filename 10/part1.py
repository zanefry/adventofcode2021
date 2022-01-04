#!/usr/bin/env python3

import sys

def main():
    lines = []
    with open(sys.argv[1]) as f:
        lines = [l.rstrip() for l in f.readlines()]

    score = 0
    stack = []
    for line in lines:
        for n, c in enumerate(line):
            if c in '([{<':
                stack.append(c)
            elif c == ')':
                if stack[-1] != '(':
                    score += 3
                    break
                else: stack.pop()
            elif c == ']':
                if stack[-1] != '[':
                    score += 57
                    break
                else: stack.pop()
            elif c == '}':
                if stack[-1] != '{':
                    score += 1197
                    break
                else: stack.pop()
            elif c == '>':
                if stack[-1] != '<':
                    score += 25137
                    break
                else: stack.pop()

    print(score)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part1.py <file>')
    main()
