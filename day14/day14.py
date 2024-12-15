import pathlib
import re

def extract_ints(raw: str) -> list[int]:
    return list(map(int, re.findall(r"((?:-|\+)?\d+)", raw)))

def is_valid(x: int, y: int, rows: int, cols: int) -> bool:
    return 0 <= x < rows and 0 <= y < cols

def first_part(input: str, rows: int, cols: int) -> int:
    matrix = []

    for i in range(rows):
        matrix.append([0] * cols)

    robots_infos = input.split('\n')

    for robot_info in robots_infos:
        y, x, dy, dx = extract_ints(robot_info)

        matrix[x][y] += 1

        for _ in range(100):
            matrix[x][y] -= 1
            nx, ny = x + dx, y + dy

            if not is_valid(nx, ny, rows, cols):
                nx = (x + dx) % rows
                ny = (y + dy) % cols

            matrix[nx][ny] += 1
            x, y = nx, ny

    first_quarter = 0
    for i in range(rows // 2):
        for j in range(cols // 2):
            if i != rows // 2 and j != cols // 2:
                first_quarter += matrix[i][j]

    second_quarter = 0
    for i in range(rows // 2):
        for j in range(cols // 2, cols):
            if i != rows // 2 and j != cols // 2:
                second_quarter += matrix[i][j]

    third_quarter = 0
    for i in range(rows // 2, rows):
        for j in range(cols // 2):
            if i != rows // 2 and j != cols // 2:
                third_quarter += matrix[i][j]

    fourth_quarter = 0
    for i in range(rows // 2, rows):
        for j in range(cols // 2, cols):
            if i != rows // 2 and j != cols // 2:
                fourth_quarter += matrix[i][j]

    return first_quarter * second_quarter * third_quarter * fourth_quarter

def second_part(input: str, rows: int, cols: int) -> int:
    robots_infos = input.split('\n')
    robots_infos = [(x, y, dx, dy) for y, x, dy, dx in map(extract_ints, robots_infos)]

    ans = 0

    while True:
        ans += 1
        pos = set()

        for i in range(len(robots_infos)):
            x, y, dx, dy = robots_infos[i]
            nx = (x + dx) % rows
            ny = (y + dy) % cols
            pos.add((nx, ny))
            robots_infos[i] = (nx, ny, dx, dy)

        if len(pos) == len(robots_infos):
            break

    return ans

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent
    # test_input = open(path.joinpath('test_input.txt'), 'r').read()
    input = open(path.joinpath('input.txt'), 'r').read()

    print('First part:')
    # print(f'Test: {first_part(test_input, 7, 11)}')
    print(f'Answer: {first_part(input, 103, 101)}')

    print()

    print('Second part:')
    # print(f'Test: {second_part(test_input, 7, 11)}')
    print(f'Answer: {second_part(input, 103, 101)}')