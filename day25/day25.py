# import sys
# from math import *
# from time import *
# from collections import *
# from heapq import *
#
#
# def part1(data):
#     keys = []
#     locks = []
#     for keylock in data:
#         m = len(keylock)
#         n = len(keylock[0])
#
#         if all(k == '#' for k in keylock[0]) and all(k == '.' for k in keylock[m - 1]):
#             lockHeights = []
#             for j in range(n):
#                 height = 0
#                 for i in range(1, m - 1):
#                     if keylock[i][j] == '#':
#                         height += 1
#                 lockHeights.append(height)
#             locks.append((lockHeights, m, n))
#         else:
#             keyHeights = []
#             for j in range(n):
#                 height = 0
#                 for i in range(1, m - 1):
#                     if keylock[i][j] == '#':
#                         height += 1
#                 keyHeights.append(height)
#             keys.append((keyHeights, m, n))
#
#     count = 0
#     for l, mL, nL in locks:
#         for k, mK, nK in keys:
#             if mL == mK and nL == nK and all([k[j] + l[j] <= mL - 2 for j in range(nL)]):
#                 count += 1
#     return count
#
#
# def part2(data):
#     pass
#
#
# if __name__ == "__main__":
#     data = []
#     with open('input.txt', 'r') as f:
#         lines = []
#         for raw_line in f:
#             line = raw_line.strip()
#             if not line:
#                 data.append(lines)
#                 lines = []
#             else:
#                 lines.append(line)
#         if lines:
#             data.append(lines)
#
#     # if sys.argv[2] == "part1":
#         print(f'Part 1 Answer = {part1(data)}')
#     # if sys.argv[2] == "part2":
#         print(f'Part 2 Answer = {part2(data)}')


import unittest
import sys


class Dec25:
    verbose = True
    locks = []
    keys = []
    size = 0

    def parse_lock(self, block):
        lock = []
        for c in range(len(block[0])):
            for r in range(len(block)):
                if block[r][c] == '#':
                    column_value = r
            lock.append(column_value)
        return tuple(lock)

    def parse_key(self, block):
        key = []
        num_rows = len(block)
        for c in range(len(block[0])):
            for r in range(num_rows):
                if block[num_rows - 1 - r][c] == '#':
                    column_value = r
            key.append(column_value)
        return tuple(key)

    def parse_block(self, block):
        if block[0][0] == '#':
            lock = self.parse_lock(block)
            self.locks.append(lock)
        else:
            key = self.parse_key(block)
            self.keys.append(key)

    def parse_input(self, inp):
        self.locks = []
        self.keys = []
        self.size = 0
        block = []
        for line_ in inp.strip().splitlines():
            line_ = line_.strip()
            if line_:
                block.append(line_)
            else:
                self.parse_block(block)
                block = []
        self.parse_block(block)
        self.size = len(block) - 1

    def lock_and_key_fit(self, lock, key):
        fit = True
        for v1, v2 in zip(lock, key):
            if v1 + v2 >= self.size:
                fit = False
        return fit

    def find_combinations(self):
        combinations = set()
        for lock in self.locks:
            for key in self.keys:
                if self.lock_and_key_fit(lock, key):
                    combinations.add((lock, key))
        return combinations

    def solve1(self, inp):
        self.parse_input(inp)
        combinations = self.find_combinations()
        return len(combinations)

    def solve2(self, inp):
        self.parse_input(inp)
        return 0


# ****************************************************************************
# Unittests
# ****************************************************************************

class TestDec25(unittest.TestCase):
    EXAMPLE_INPUT = """
    #####
    .####
    .####
    .####
    .#.#.
    .#...
    .....

    #####
    ##.##
    .#.##
    ...##
    ...#.
    ...#.
    .....

    .....
    #....
    #....
    #...#
    #.#.#
    #.###
    #####

    .....
    .....
    #.#..
    ###..
    ###.#
    ###.#
    #####

    .....
    .....
    .....
    #....
    #.#..
    #.#.#
    #####
    """

    def setUp(self):
        self.solver = Dec25()
        self.solver.verbose = '-v' in sys.argv

    def print(self, output):
        if '-v' in sys.argv:
            print(output, end=' ')
            sys.stdout.flush()
        else:
            print(f'{self.id()} = {output}')

    @staticmethod
    def get_input():
        with open('input.txt', 'r') as f:
            return f.read()

    def test_parse(self):
        self.solver.parse_input(self.EXAMPLE_INPUT)
        self.assertEqual(self.solver.locks, [(0, 5, 3, 4, 3), (1, 2, 0, 5, 3)])
        self.assertEqual(self.solver.keys, [(5, 0, 2, 1, 3), (4, 3, 4, 0, 2), (3, 0, 2, 0, 1)])

    def test_example1(self):
        output = self.solver.solve1(self.EXAMPLE_INPUT)
        self.assertEqual(output, 3)

    def test_solution1(self):
        output = self.solver.solve1(self.get_input())
        self.assertNotEqual(output, 3302)
        self.print(output)

    def test_solution2(self):
        output = self.solver.solve2(self.get_input())
        self.print(output)


if __name__ == '__main__':
    unittest.main()