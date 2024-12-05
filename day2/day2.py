import sys
import os

# https://adventofcode.com/2024/day/2

def partOne():
  readings = parseInput()
  validCount = 0
  for reading in readings:
    if valid(reading):
      validCount += 1
  print(validCount)

def partTwo():
  readings = parseInput()
  validCount = 0
  for reading in readings:
    if valid(reading):
      validCount += 1
    else:
      for i in range(len(reading)):
        readingCopy = list(reading)
        del readingCopy[i]
        if valid(readingCopy):
          validCount += 1
          break
  print(validCount)

def valid(reading):
  up = reading[0] <= reading[1]
  for i in range(len(reading) - 1):
    diff = reading[i + 1] - reading[i]
    if up and (diff < 1 or diff > 3):
      return False
    if not up and (diff > -1 or diff < -3):
      return False
  return True

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  input = open(f'{dir_path}/input.txt', 'r').read()
  readings = []
  for row in input.splitlines():
    pieces = row.split(" ")
    readings.append([int(piece) for piece in pieces])
  return readings

partOne()

partTwo()