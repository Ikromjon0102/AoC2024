####################################################################################
#
# Advent of Code 2024 Framework (c) Simon Perkins MA FCA FBP Dec 2021 to Dec 2024
#
####################################################################################

import time
import types
import sys

prog_start_time = 0
vanswer1 = vanswer2 = None

def read_file(filename, isnumlist, printme, nolines): # function to read in the input file with the day's puzzle input
    with open(filename, "r") as fp:
        if nolines:
            Text = fp.read()
            return Text
        Lines = fp.readlines()
        if(isnumlist):
            Lines=[' '.join(line.split()) for line in Lines]   # Useful for removing extra white space in arrays of numbers e.g.
        else:
            Lines=[line.rstrip() for line in Lines]            # Useful for text list
    numlines, linelen = len(Lines), len(Lines[0])
    if printme:
        print("Read in a total of ",numlines,"lines of data.")
        print("First line:", Lines[0])
        print("Last line:", Lines[-1], "\n")
    return Lines, numlines, linelen

def pad_data(dat_tuple, pad, padchar):
    if pad > 0:
        (data, numlines, linelen) = dat_tuple
        ret_data, padlinelen = [], linelen + 2 * pad
        for i in range(pad):
            ret_data.append(padchar * padlinelen)
        for line in data:
            ret_data.append(padchar * pad + line + padchar * pad)
        for i in range(pad):
            ret_data.append(padchar * padlinelen)
        return ret_data, numlines, linelen
    else:
        return dat_tuple

def Init(filename, isnumlist=False, printme=False, nolines=False, test=False, pad=0, padchar=' '):
    global prog_start_time
    print("\n2024 Advent of Code - Framework running...\n")
    prog_start_time = time.perf_counter()
    if test:
        return pad_data(read_file('data/test.txt', isnumlist, printme, nolines), pad, padchar)
    elif filename:
        return pad_data(read_file(filename, isnumlist, printme, nolines), pad, padchar)
    else:
        return None, 0

def verify(answer1, answer2=None):
    global vanswer1, vanswer2
    vanswer1, vanswer2 = answer1, answer2

def run(answer1, answer2=None):  # will accept a tuple, or either 1 or 2 answers or fn calls that give answers 
    global prog_start_time
    if type(answer1) == tuple:
        (answer1, answer2) = answer1
    if isinstance(answer1, types.FunctionType) and answer2 == None and vanswer2 is not None:
        answer = answer1()
        if type(answer) == tuple:
            (answer1, answer2) = answer
    if isinstance(answer1, types.FunctionType):
        print("Part 1 answer is: ", answer1())
    else:
        print("Part 1 answer is: ", answer1)
    if vanswer1 is not None:
        print("Verified answer : ", vanswer1, "\n")
    prog1_end_time = time.perf_counter()
    print("Elapsed time:", prog1_end_time - prog_start_time, "\n")
    sys.stdout.flush()
    if isinstance(answer2, types.FunctionType):
        print("Part 2 answer is: ", answer2())
    else:
        print("Part 2 answer is: ", answer2)
    if vanswer2 is not None:
        print("Verified answer : ", vanswer2, "\n")
    prog2_end_time = time.perf_counter()
    print("Elapsed time:", prog2_end_time - prog1_end_time)
    print("Total elapsed time:", prog2_end_time - prog_start_time, "\n")

def get_grid(Lines, isint=False):
    grid = []
    if isint is False:
        grid = [[ch for ch in line] for line in Lines]
    else:
        grid =[[int(ch) for ch in line] for line in Lines]
    return grid