import sys
import os
from functools import cmp_to_key


# https://adventofcode.com/2024/day/5

def partOne():
    rules, updates = parseInput()
    count = 0
    for update in updates:
        valid = True
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                a = update[i]
                b = update[j]
                if b in rules['after'] and a in rules['after'][b]:
                    valid = False
                    break
                if a in rules['before'] and b in rules['before'][a]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            print(update)
            count += int(update[len(update) // 2])
    print(count)


def partTwo():
    rules, updates = parseInput()
    count = 0
    for update in updates:
        valid = True
        swaps = []
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                a = update[i]
                b = update[j]
                if b in rules['after'] and a in rules['after'][b]:
                    valid = False
                    break
                if a in rules['before'] and b in rules['before'][a]:
                    valid = False
                    break
            if not valid:
                break

        def compare(a, b):
            if b in rules['after'] and a in rules['after'][b]:
                return -1
            if a in rules['before'] and b in rules['before'][a]:
                return -1
            return 1

        if not valid:
            update = sorted(update, key=cmp_to_key(compare))
            count += int(update[len(update) // 2])
    print(count)


def parseInput():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    lines = open(f'{dir_path}/input.txt', 'r').read().splitlines()
    rules = {'after': {}, 'before': {}}
    updates = []
    emptySeen = False
    for line in lines:
        if line == '':
            emptySeen = True
            continue
        if emptySeen:
            updates.append(line.split(','))
        else:
            a, b = line.split('|')
            if a not in rules['after']:
                rules['after'][a] = set()
            if b not in rules['before']:
                rules['before'][b] = set()
            rules['after'][a].add(b)
            rules['before'][b].add(a)
    return rules, updates


partOne()

partTwo()