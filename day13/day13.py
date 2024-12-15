import re


def win(a1, b1, c1, a2, b2, c2, add=0):
    c1 += add
    c2 += add
    if (det := a1 * b2 - a2 * b1) != 0:
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        if x == int(x) and y == int(y):
            return int(3 * x + y)
    return 0


claw_machines = list()
with open("input.txt") as f:
    for instructions in f.read().split("\n\n"):
        A_button, B_button, prize = instructions.splitlines()
        Ax, Ay = map(int, re.findall(r"\d+", A_button))
        Bx, By = map(int, re.findall(r"\d+", B_button))
        prize_x, prize_y = map(int, re.findall(r"\d+", prize))
        claw_machines.append((Ax, Bx, prize_x, Ay, By, prize_y))


# ==== PART 1 ====
print(sum(win(*m) for m in claw_machines))


# ==== PART 2 ====
print(sum(win(*m, add=10000000000000) for m in claw_machines))