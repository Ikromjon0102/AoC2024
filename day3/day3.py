import sys
import os
import re

# https://adventofcode.com/2024/day/3

def partOne():
  txt = parseInput()
  matches = re.findall("mul\([1-9]\d{0,2},[1-9]\d{0,2}\)", txt)
  sum = 0
  for match in matches:
    X, Y = [int(val) for val in match[4:-1].split(",")]
    # print(X, Y)
    sum += X * Y
  print(sum)

def partTwo():
  txt = parseInput()
  matches = re.findall("(mul\([1-9]\d{0,2},[1-9]\d{0,2}\)|do\(\)|don't\(\))", txt)
  sum = 0
  enabled = True
  for match in matches:
    if match[0] == "d":
      enabled = match == "do()"
      continue
    if not enabled:
      continue
    X, Y = [int(val) for val in match[4:-1].split(",")]
    sum += X * Y
  print(sum)

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return open(f'{dir_path}/input.txt', 'r').read()

# partOne()
partTwo()
