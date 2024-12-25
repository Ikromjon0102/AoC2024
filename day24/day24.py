from more_itertools import *
import timeit

SAMPLE = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

def parse(input):
    initials, rules = input.split('\n\n')
    initial_values = {vs[0]: int(vs[1])
                      for line in initials.splitlines()
                      for vs in [line.split(': ')]}
    rules = {vs[4]: (vs[0], vs[1], vs[2])
                     for line in rules.splitlines()
                     for vs in [line.split(' ')]}
    return rules, initial_values


def compute(wire, rules, initial_values):
    if wire in rules:
        rule = rules[wire]
        match rule[1]:
            case 'AND':
                return compute(rule[0], rules, initial_values) & compute(rule[2], rules, initial_values)
            case 'OR':
                return compute(rule[0], rules, initial_values) | compute(rule[2], rules, initial_values)
            case 'XOR':
                return compute(rule[0], rules, initial_values) ^ compute(rule[2], rules, initial_values)
            case _:
                raise Exception(f"unknown operator {rule[1]}")
    else:
        return initial_values[wire]


def part1(input):
    rules, initial_values = parse(input)

    power = 1
    result = 0
    for wire in sorted(rules.keys()):
        if wire.startswith('z'):
            bit = compute(wire, rules, initial_values)
            result += power * bit
            power *= 2

    return result


def part2(input):
    rules, initial_values = parse(input)

    expecteds = {}
    oldleft = ""
    for wire in sorted(rules.keys()):
        if not wire.startswith("z"):
            continue
        bit = int(wire[1:])
        if bit == 0:
            expr = "(x00 XOR y00)"
        else:
            if bit == 1:
                left = f"(x{bit-1:02} AND y{bit-1:02})"
            else:
                left = f"(({oldleft} AND (x{bit-1:02} XOR y{bit-1:02})) OR (x{bit-1:02} AND y{bit-1:02}))"
            oldleft = left
            if f"z{bit+1:02}" in rules:
                expr = f"({left} XOR (x{bit:02} XOR y{bit:02}))"
            else:
                expr = left
        expecteds[wire] = expr

    def make_expr(wire0):
        seen = set()
        def recur(wire):
            if wire not in rules:
                return wire
            if wire in seen:
                return "LOOP"
            seen.add(wire)
            rule = rules[wire]
            expr_left = recur(rule[0])
            expr_right = recur(rule[2])
            expr_left, expr_right = sorted((expr_left, expr_right))
            return f"({expr_left} {rule[1]} {expr_right})"

        return recur(wire0), seen

    def swap(a,b):
        rules[a], rules[b] = rules[b], rules[a]

    swapped = set()
    swappable = set(rules.keys())
    for wire in sorted(rules.keys()):
        if not wire.startswith('z'):
            continue
        expected = expecteds[wire]
        expr, used = make_expr(wire)
        if expr != expected:
            print("fixing", wire)
            for a, b in distinct_combinations(swappable, 2):
                swap(a, b)
                expr, used = make_expr(wire)
                if expr == expected:
                    print(f"{wire} fixed by {a} <-> {b}")
                    swapped |= { a, b }
                    break
                else:
                    swap(a, b)
        swappable -= used

    return ','.join(sorted(swapped))


def test_part1():
    assert part1(SAMPLE) == 2024


if __name__ == '__main__':
    inputfile = 'input.txt'
    INPUT = open(inputfile, "r").read()

    result = part1(INPUT)
    print("part1:", result)
    assert result == 59336987801432

    result = part2(INPUT)
    print("part2:", result)
    assert result == 'ctg,dmh,dvq,rpb,rpv,z11,z31,z38'

    num, total = timeit.Timer(lambda: part2(INPUT)).autorange()
    print("time=", total / num)