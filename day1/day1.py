import sys
import os


# https://adventofcode.com/2024/day/1

def partOne():
    left, right = parseInput()
    left.sort()
    right.sort()
    score = 0
    for i in range(len(left)):
        score += abs(left[i] - right[i])
    print(score)


def partTwo():
    left, right = parseInput()
    count = {}
    for num in right:
        count[num] = count.get(num, 0) + 1
    score = 0
    for num in left:
        score += num * count.get(num, 0)
    print(score)


def parseInput():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input = open(f'{dir_path}/input.txt', 'r').read()
    left = []
    right = []
    for row in input.splitlines():
        pieces = row.split("   ")
        left.append(int(pieces[0]))
        right.append(int(pieces[1]))

    return left, right


partOne()
partTwo()