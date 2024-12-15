# grid = {}
#
# robot_coords = None
# dim = None
#
# with open('input.txt') as infile:
#     map, commands = infile.read().split('\n\n')
#     for x, line in enumerate(map.strip('\n').split('\n')):
#         for y, char in enumerate(line.strip()):
#             if char == '@':
#                 robot_coords = (x, y)
#             elif char != '.':
#                 grid[(x, y)] = char
#             dim = (x, y)
#
# directions = {
#     '^': (-1, 0),
#     'v': (1, 0),
#     '>': (0, 1),
#     '<': (0, -1)
# }
#
# def can_move(c, d):
#     nx, ny = (c[0]+d[0], c[1] + d[1])
#     n = (nx, ny)
#     if n not in grid:
#         return True
#     if grid[n] == '#':
#         return False
#     return can_move(n, d)
#
# def do_move(c, d):
#     n = (c[0]+d[0], c[1] + d[1])
#     if n in grid:
#        do_move(n, d)
#     if grid.get(c) is not None:
#         grid[n] = grid.pop(c)
#
# for move in commands:
#     if move not in directions:
#         continue
#     d = directions[move]
#     if can_move(robot_coords, d):
#         do_move(robot_coords, d)
#         robot_coords = (robot_coords[0] + d[0], robot_coords[1] + d[1])
#
# total = 0
# for coord, item in grid.items():
#     if item == 'O':
#         x, y = coord
#         total += 100*x + y
#
# print(total)


grid = {}

dim = None
robot_coords = None

with open('input.txt') as infile:
    map, commands = infile.read().split('\n\n')
    for x, line in enumerate(map.strip('\n').split('\n')):
        for y, char in enumerate(line.strip()):
            dim = (x + 1, 2 * y + 1 + 1)
            if char == '@':
                robot_coords = (x, 2 * y)
            elif char == '.':
                continue
            elif char == 'O':
                grid[(x, 2 * y)] = char
            elif char == '#':
                grid[((x, 2 * y))] = char
                grid[((x, 2 * y + 1))] = char

directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1)
}


def printgrid():
    for x in range(dim[0]):
        for y in range(dim[1]):
            other = (x, y - 1)
            c = (x, y)
            if robot_coords == c:
                print('@', end='')
            elif grid.get(other) == 'O':
                print(']', end='')
            elif grid.get(c) == 'O':
                print('[', end='')
            elif grid.get(c) is not None:
                print(grid.get(c), end='')
            else:
                print(' ', end='')
        print()


def box(c):
    if grid.get(c) == 'O':
        other = (c[0], c[1] + 1)
        return [c, other]
    other = (c[0], c[1] - 1)
    if grid.get(other) == 'O':
        return [other, c]
    return None


def can_move(c, d):
    nx, ny = (c[0] + d[0], c[1] + d[1])
    n = (nx, ny)
    if grid.get(n) == '#':
        return False
    maybe_box = box(n)
    if maybe_box is None:
        return True
    if d == (0, -1):
        return can_move(maybe_box[0], d)
    elif d == (0, 1):
        return can_move(maybe_box[1], d)
    else:
        return can_move(maybe_box[0], d) and can_move(maybe_box[1], d)


def do_move(c, d):
    nx, ny = (c[0] + d[0], c[1] + d[1])
    n = (nx, ny)
    maybe_box = box(n)
    if maybe_box is not None:
        if d == (0, -1):
            do_move(maybe_box[0], d)
        elif d == (0, 1):
            do_move(maybe_box[1], d)
            grid[maybe_box[1]] = grid.pop(maybe_box[0])
        else:
            do_move(maybe_box[1], d)
            do_move(maybe_box[0], d)
    if grid.get(c) is not None:
        grid[n] = grid.pop(c)


for move in commands:
    if move not in directions:
        continue
    d = directions[move]
    if can_move(robot_coords, d):
        do_move(robot_coords, d)
        robot_coords = (robot_coords[0] + d[0], robot_coords[1] + d[1])

printgrid()

total = 0
for coord, item in grid.items():
    if item == 'O':
        x, y = coord
        total += 100 * x + y

print(total)