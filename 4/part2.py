#!/usr/bin/python3

import sys

def has_bingo(board: list[list[list]]) -> bool:
    for row in board:
        if all([n[1] for n in row]):
            return True

    for col in [[row[i] for row in board] for i in range(5)]:
        if all([n[1] for n in col]):
            return True

    return False

def final_score(board: list[list[list]], lastnum: int) -> int:
    sum = 0
    for row in board:
        for n in row:
            if not n[1]: sum += n[0]
    return sum * lastnum

def main():
    parts = []
    with open(sys.argv[1]) as f:
        parts = f.read().rstrip().split('\n\n')

    called_nums = [int(n) for n in parts[0].split(',')]
    boards = [[[[int(n), False] for n in row.split()] \
            for row in board.split('\n')] \
            for board in parts[1:]]

    no_bingo = set(range(len(boards)))

    for current_num in called_nums:
        # update boards
        for board in [boards[i] for i in no_bingo]:
            for i in range(5):
                for j in range(5):
                    if board[i][j][0] == current_num:
                        board[i][j][1] = True

        # remove bingos
        for n in list(no_bingo):
            if has_bingo(boards[n]):
                no_bingo.remove(n)

                if not no_bingo:
                    print(final_score(boards[n], current_num))

if __name__ == "__main__":l
    if len(sys.argv) != 2:
        sys.exit('usage: ./part1.py <inputfile>')
    main()
