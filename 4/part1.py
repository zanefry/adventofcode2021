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

def main():
    parts = []
    with open(sys.argv[1]) as f:
        parts = f.read().rstrip().split('\n\n')

    called_nums = [int(n) for n in parts[0].split(',')]
    boards = [[[[int(n), False] for n in row.split()] \
            for row in board.split('\n')] \
            for board in parts[1:]]

    for current_num in called_nums:
        # update boards
        for board in boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j][0] == current_num:
                        board[i][j][1] = True

        # check for bingo
        for n in range(len(boards)):
            if has_bingo(boards[n]):
                print(f'board {n} has bingo')

                final_score = 0
                for row in boards[n]:
                    for n in row:
                        if not n[1]: final_score += n[0]
                final_score *= current_num

                print(f'{final_score=}')
                return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('usage: ./part1.py <inputfile>')
    main()
