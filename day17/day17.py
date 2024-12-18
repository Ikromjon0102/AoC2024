ip = 0


def run(progr, reg, i, part2=True):
    global ip
    ip = 0
    output = []
    if part2:
        reg[0] = i

    def comboOp(x):
        if 0 <= x <= 3:
            return x
        if x == 4:
            return reg[0]
        if x == 5:
            return reg[1]
        if x == 6:
            return reg[2]
        assert (False)

    def adv(x):
        reg[0] = (reg[0] // (2 ** comboOp(x)))

    def bxl(x):
        reg[1] = reg[1] ^ x

    def bst(x):
        reg[1] = comboOp(x) % 8

    def jnz(x):
        global ip
        if reg[0] != 0:
            ip = x
        else:
            ip += 2

    def bxc(x):
        reg[1] = reg[1] ^ reg[2]

    def out(x):
        output.append(comboOp(x) % 8)

    def bdv(x):
        reg[1] = reg[0] // (2 ** comboOp(x))

    def cdv(x):
        reg[2] = reg[0] // (2 ** comboOp(x))

    instr = [
        lambda x: adv(x),
        lambda x: bxl(x),
        lambda x: bst(x),
        lambda x: jnz(x),
        lambda x: bxc(x),
        lambda x: out(x),
        lambda x: bdv(x),
        lambda x: cdv(x)
    ]

    while 0 <= ip < len(progr):
        cur = progr[ip]
        if ip + 1 in range(len(progr)):
            inp = progr[ip + 1]
        instr[cur](inp)
        if cur != 3:
            ip += 2
    return output


def solve(program, regs):
    stack = []
    for i in range(1, 8):
        stack.append(i)
    res = []
    while stack:
        i = stack.pop()
        curOutput = run(program, [r for r in regs], i)
        if len(curOutput) < len(program) and curOutput == program[-len(curOutput):]:
            for j in range(8):
                stack.append(i * 8 + j)
        elif curOutput == program:
            res.append(i)
    return min(res)


with open("input.txt", "r") as inputFile:
    inp = inputFile.read().split('\n\n')
    reg = [0] * 3
    progr = []
    for part in inp:
        for i, line in enumerate(part.splitlines()):
            if line.startswith('Program'):
                progr = [int(x) for x in line.split()[-1].split(',')]
            elif line.startswith('Reg'):
                reg[i] = int(line.split()[-1])

    print(','.join(str(c) for c in run(progr, [r for r in reg], 0, False)))
    print(solve(progr, reg))