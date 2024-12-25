from collections import deque

def parse():
    return [list(line) for line in open("input.txt").read().splitlines()]

grid = parse()
ROWS, COLS = len(grid), len(grid[0])

def is_valid(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def find_positions():
    start = end = None
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)
    return start, end

def bfs_with_distances(start):
    queue = deque([start])
    distances = [[float('inf')] * COLS for _ in range(ROWS)]
    distances[start[0]][start[1]] = 0

    while queue:
        r, c = queue.popleft()
        current_distance = distances[r][c]
        for nr, nc in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
            if not is_valid(nr, nc):
                continue
            if grid[nr][nc] != '#' and distances[nr][nc] > current_distance + 1:
                distances[nr][nc] = current_distance + 1
                queue.append((nr, nc))

    return distances


def part1():
    start, end = find_positions()

    end_distances = bfs_with_distances(end)
    start_distances = bfs_with_distances(start)

    original_distance = end_distances[start[0]][start[1]]
    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '#':
                continue

            if start_distances[r][c] == float('inf'):
                continue

            for dr in range(-2, 3): # can travel 2 steps in any direction
                for dc in range(-2, 3):
                    if abs(dr) + abs(dc) > 2:
                        continue
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc) and grid[nr][nc] != '#' and end_distances[nr][nc] < float('inf'):
                        new_distance = start_distances[r][c] + end_distances[nr][nc] + 2
                        if (new_distance + 100) <= original_distance:
                            count += 1

    return count

def part2():
    start, end = find_positions()

    end_distances = bfs_with_distances(end)
    start_distances = bfs_with_distances(start)

    original_distance = end_distances[start[0]][start[1]]
    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '#':
                continue

            if start_distances[r][c] == float('inf'):
                continue

            for dr in range(-20, 21): # can travel 20 steps in any direction
                for dc in range(-20, 21):
                    if abs(dr) + abs(dc) > 20:
                        continue

                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc) and grid[nr][nc] != '#' and end_distances[nr][nc] < float('inf'):
                        new_distance = start_distances[r][c] + end_distances[nr][nc] + abs(dr) + abs(dc)
                        if (new_distance + 100) <= original_distance:
                            count += 1

    return count

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")