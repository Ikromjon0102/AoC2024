from itertools import *
from more_itertools import *
import re
from functools import partial, cmp_to_key
from collections import defaultdict
from math import gcd, sqrt
from heapq import *
import timeit
import functools

SAMPLE = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

SAMPLE2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

def parse(input):
    matrix = input.splitlines()
    width = len(matrix[0])
    height = len(matrix)
    walls = set()
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == '#':
                walls.add((i, j))
            elif cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    return walls, start, end, width, height

def neighbors(i, j):
    return [ (i, j+1), (i+1, j), (i, j-1), (i-1, j) ]

DIRS = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]

def findcosts(start, walls):
    costs = { (start, 0): 0 }
    frontier = [ (start, 0) ]
    timeout = 4000000
    steps = 0
    while len(frontier) > 0 and steps < timeout:
        steps += 1
        nextfrontier = []
        for ((i, j), d) in frontier:
            cost = costs[((i,j),d)]
            for (ni, nj), nd, ncost in [
                   ((i + DIRS[d][0], j + DIRS[d][1]), d, cost + 1),
                   ((i, j), (d + 1) % 4, cost + 1000),
                   ((i, j), (d - 1) % 4, cost + 1000)
                ]:
                if (ni, nj) in walls:
                    continue
                if ((ni, nj), nd) in costs and \
                   costs[((ni, nj), nd)] <= ncost:
                    continue

                costs[((ni, nj), nd)] = ncost
                nextfrontier.append(((ni, nj), nd))
        frontier = nextfrontier

    if steps >= timeout:
        raise Exception("timedout")

    return costs


def part1(input):
    maze = parse(input)
    walls, start, end, width, height = maze

    costs = findcosts(start, walls)

    return min(costs[(end, d)] for d in range(4))


def part2(input):
    maze = parse(input)
    walls, start, end, width, height = maze

    costs = findcosts(start, walls)

    bestcost = min(costs[(end, d)] for d in range(4))

    frontier = [ (end, d)
                for d in range(4)
                if costs[(end, d)] == bestcost ]
    timeout = 4000000
    steps = 0
    bestcells = set(pos for (pos, d) in frontier)
    while len(frontier) > 0 and steps < timeout:
        steps += 1
        nextfrontier = []
        for ((i, j), d) in frontier:
            cost = costs[((i,j),d)]
            for (ni, nj), nd, ncost in [
                   ((i - DIRS[d][0], j - DIRS[d][1]), d, cost - 1),
                   ((i, j), (d + 1) % 4, cost - 1000),
                   ((i, j), (d - 1) % 4, cost - 1000)
                ]:
                if (ni, nj) in walls:
                    continue
                if costs[((ni, nj), nd)] != ncost:
                    continue
                nextfrontier.append(((ni, nj), nd))
                bestcells.add((ni, nj))
        frontier = nextfrontier

    return len(bestcells)


def test_part1():
    assert part1(SAMPLE) == 7036


def test_part2():
    assert part2(SAMPLE) == 45


def test_part2_2():
    assert part2(SAMPLE2) == 64


if __name__ == '__main__':
    inputfile = 'input.txt'
    INPUT = open(inputfile, "r").read()

    result = part1(INPUT)
    print("part1:", result)
    # assert result == 90460

    result = part2(INPUT)
    print("part2:", result)
    # assert result == 575

    num, total = timeit.Timer(lambda: part2(INPUT)).autorange()
    print("time=", total / num)