import sys
import os


# https://adventofcode.com/2024/day/8

def partOne():
    grid = parseInput()
    row = len(grid)
    col = len(grid[0])
    # print(grid)
    ants_map = {}
    for i in range(row):
        for j in range(col):
            cell = grid[i][j]
            if cell == '.':
                continue
            if cell not in ants_map:
                ants_map[cell] = []
            ants_map[cell].append([i, j])
    stuns = set()
    for ant in ants_map:
        ants = ants_map[ant]
        count = len(ants)
        for i in range(count):
            A = ants[i]
            for j in range(i + 1, count):
                B = ants[j]
                diff = [A[0] - B[0], A[1] - B[1]]
                Ai, Aj = A[0] + diff[0], A[1] + diff[1]
                Bi, Bj = B[0] - diff[0], B[1] - diff[1]
                if Ai >= 0 and Ai < row and Aj >= 0 and Aj < col:
                    stuns.add(Ai * col + Aj)
                if Bi >= 0 and Bi < row and Bj >= 0 and Bj < col:
                    stuns.add(Bi * col + Bj)
    print(len(stuns))


def partTwo():
    grid = parseInput()
    row = len(grid)
    col = len(grid[0])
    # print(grid)
    ants_map = {}
    for i in range(row):
        for j in range(col):
            cell = grid[i][j]
            if cell == '.':
                continue
            if cell not in ants_map:
                ants_map[cell] = []
            ants_map[cell].append([i, j])
    stuns = set()
    for ant in ants_map:
        ants = ants_map[ant]
        count = len(ants)
        for i in range(count):
            A = ants[i]
            stuns.add(A[0] * col + A[1])
            for j in range(i + 1, count):
                B = ants[j]
                diff = [A[0] - B[0], A[1] - B[1]]
                Ai, Aj = A
                while True:
                    Ai, Aj = Ai + diff[0], Aj + diff[1]
                    if valid(Ai, Aj, row, col):
                        stuns.add(Ai * col + Aj)
                    else:
                        break

                Bi, Bj = B
                while True:
                    Bi, Bj = Bi - diff[0], Bj - diff[1]
                    if valid(Bi, Bj, row, col):
                        stuns.add(Bi * col + Bj)
                    else:
                        break
    print(len(stuns))


def valid(Ai, Aj, row, col):
    return Ai >= 0 and Ai < row and Aj >= 0 and Aj < col


def parseInput():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return [list(line) for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]


partOne()


partTwo()