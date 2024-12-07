import sys
import os
from functools import cmp_to_key


# https://adventofcode.com/2024/day/6

def partOne():
    grid = parseInput()
    points = set()
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dir = 0
    si = -1
    sj = -1
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '^':
                si, sj = i, j

    points.add(si * col + sj)

    while True:
        ni, nj = si + dirs[dir][0], sj + dirs[dir][1]
        if ni < 0 or ni >= row or nj < 0 or nj >= col:
            break
        if grid[ni][nj] == '#':
            dir = (dir + 1) % 4
            continue
        si, sj = ni, nj
        points.add(si * col + sj)
    print(len(points))


def partTwo():
    grid = parseInput()
    si = -1
    sj = -1
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '^':
                si, sj = i, j

    count = 0
    # God, please forgive my sins!
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '.':
                grid[i][j] = '#'
                # print('checking for loop:', i, j)
                count += 1 if hasLoop(grid, si, sj, row, col) else 0
                grid[i][j] = '.'

    # for i in range(row):
    #   for j in range(col):
    #     print(grid[i][j], end="")
    #   print()
    print(count)


def hasLoop(grid, si, sj, row, col):
    past = [[set() for j in range(col)] for i in range(row)]
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dir = 0
    while True:
        if dir in past[si][sj]:
            return True
        else:
            past[si][sj].add(dir)
        ni, nj = si + dirs[dir][0], sj + dirs[dir][1]
        if ni < 0 or ni >= row or nj < 0 or nj >= col:
            break
        if grid[ni][nj] == '#':
            dir = (dir + 1) % 4
            continue
        si, sj = ni, nj
    return False


def parseInput():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return [list(line) for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]


# partOne()

partTwo()