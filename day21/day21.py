# # Define the keypad layout
# keypad = [
#     [7, 8, 9],
#     [4, 5, 6],
#     [1, 2, 3],
#     [0, 'A', '']
# ]
#
# # Map numbers to their positions
# key_positions = {}
# for r in range(len(keypad)):
#     for c in range(len(keypad[r])):
#         if keypad[r][c] != '':
#             key_positions[keypad[r][c]] = (r, c)
#
#         # Function to calculate the distance between two keys
#
#
# def calculate_distance(start, end):
#     start_pos = key_positions[start]
#     end_pos = key_positions[end]
#     return abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])
#
#
# # Function to get the movement sequence for a specific code
# def get_movement_sequence(code):
#     sequence_length = 0
#     current_key = (0, 1)  # Starting at '5' (row 1, column 1) i.e., keypad[1][1]
#
#     for char in code:
#         if char == 'A':
#             target_key = 'A'
#         else:
#             target_key = int(char)
#
#             # Calculate distance and update sequence length
#         dist = calculate_distance(keypad[current_key[0]][current_key[1]], target_key)
#         sequence_length += dist + 1  # +1 for pressing the key
#         # Move to target key position
#         current_key = key_positions[target_key]
#
#     return sequence_length
#
#
# # Calculate complexity for each code
# codes = ['540A', '582A', '169A', '593A', '579A']
# total_complexity = 0
#
# for code in codes:
#     numeric_part = int(code[:-1])  # Get the numeric part by removing 'A'
#     length_of_sequence = get_movement_sequence(code)
#     complexity = length_of_sequence * numeric_part
#     total_complexity += complexity
#     print(f"Code: {code}, Length of Sequence: {length_of_sequence}, Complexity: {complexity}")
#
# # Print the total complexity
# print(f"Total Complexity: {total_complexity}")
# # codes = ["540A", "582A", "169A", "593A", "579A"]

#
# from collections import deque
#
#
# def find_shortest_path(start, end, keypad):
#     """
#     Finds the shortest path between two keys on a keypad.
#
#     Args:
#     start (tuple): Starting position (row, col).
#     end (tuple): Ending position (row, col).
#     keypad (list): 2D list representing the keypad layout.
#
#     Returns:
#     int: Length of the shortest path.
#     str: Sequence of moves to reach the destination.
#     """
#     moves = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
#     queue = deque([(start, "")])  # (current position, path)
#     visited = set()
#
#     while queue:
#         (cur_row, cur_col), path = queue.popleft()
#
#         if (cur_row, cur_col) == end:
#             return len(path), path
#
#         if (cur_row, cur_col) in visited:
#             continue
#         visited.add((cur_row, cur_col))
#
#         for move, (dr, dc) in moves.items():
#             new_row, new_col = cur_row + dr, cur_col + dc
#
#             # Check bounds and ensure we're not moving to a gap
#             if 0 <= new_row < len(keypad) and 0 <= new_col < len(keypad[0]) and keypad[new_row][new_col] != " ":
#                 queue.append(((new_row, new_col), path + move))
#
#     return float("inf"), ""  # In case no path is found (shouldn't happen)
#
#
# def calculate_complexity(codes, keypad):
#     """
#     Calculates the sum of complexities for a list of codes.
#
#     Args:
#     codes (list): List of codes to type.
#     keypad (list): 2D list representing the keypad layout.
#
#     Returns:
#     int: Total complexity.
#     """
#     position_map = {}
#     for r, row in enumerate(keypad):
#         for c, val in enumerate(row):
#             if val != " ":
#                 position_map[val] = (r, c)
#
#     total_complexity = 0
#     for code in codes:
#         current_position = position_map["A"]  # Start at A
#         total_presses = 0
#
#         print(f"Processing code: {code}")
#
#         for char in code:
#             target_position = position_map[char]
#             presses, path = find_shortest_path(current_position, target_position, keypad)
#             total_presses += presses
#             print(f"Move from {current_position} to {target_position}: path = {path}, presses = {presses}")
#             current_position = target_position
#
#         numeric_value = int(code[:-1])  # Remove trailing A for numeric value
#         print(f"Numeric value: {numeric_value}, Total presses: {total_presses}")
#         total_complexity += total_presses * numeric_value
#
#     return total_complexity
#
#
# # Define the keypad layout
# keypad = [
#     ["7", "8", "9"],
#     ["4", "5", "6"],
#     ["1", "2", "3"],
#     [" ", "0", "A"]
# ]
#
# # Input codes
# codes = ["540A", "582A", "169A", "593A", "579A"]
#
# # Calculate the total complexity
# total_complexity = calculate_complexity(codes, keypad)
# print("Total Complexity:", total_complexity)


# from collections import deque
# from typing import Dict, List, Set, Tuple
#
#
# def get_neighbors(pos: Tuple[int, int], keypad_type: str) -> List[Tuple[int, int]]:
#     """Get valid neighboring positions on the specified keypad type."""
#     if keypad_type == "directional":
#         valid_positions = {
#             (0, 1): "^", (1, 0): "<", (1, 1): "v", (1, 2): ">", (0, 2): "A"
#         }
#     else:  # numeric
#         valid_positions = {
#             (0, 0): "7", (0, 1): "8", (0, 2): "9",
#             (1, 0): "4", (1, 1): "5", (1, 2): "6",
#             (2, 0): "1", (2, 1): "2", (2, 2): "3",
#             (3, 1): "0", (3, 2): "A"
#         }
#
#     x, y = pos
#     neighbors = []
#     for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         new_pos = (x + dx, y + dy)
#         if new_pos in valid_positions:
#             neighbors.append(new_pos)
#     return neighbors
#
#
# def find_shortest_path(start: Tuple[int, int], target: Tuple[int, int], keypad_type: str) -> List[str]:
#     """Find shortest path between two positions on specified keypad."""
#     queue = deque([(start, [])])
#     visited = {start}
#
#     while queue:
#         pos, path = queue.popleft()
#         if pos == target:
#             return path
#
#         for next_pos in get_neighbors(pos, keypad_type):
#             if next_pos not in visited:
#                 visited.add(next_pos)
#                 new_path = path + [get_direction(pos, next_pos)]
#                 queue.append((next_pos, new_path))
#     return []
#
#
# def get_direction(from_pos: Tuple[int, int], to_pos: Tuple[int, int]) -> str:
#     """Get direction symbol for moving from one position to another."""
#     dx = to_pos[0] - from_pos[0]
#     dy = to_pos[1] - from_pos[1]
#     if dx == 1: return "v"
#     if dx == -1: return "^"
#     if dy == 1: return ">"
#     if dy == -1: return "<"
#     return ""
#
#
# def get_position(char: str, keypad_type: str) -> Tuple[int, int]:
#     """Get position coordinates for a character on specified keypad."""
#     if keypad_type == "directional":
#         positions = {
#             "^": (0, 1), "<": (1, 0), "v": (1, 1),
#             ">": (1, 2), "A": (0, 2)
#         }
#     else:  # numeric
#         positions = {
#             "7": (0, 0), "8": (0, 1), "9": (0, 2),
#             "4": (1, 0), "5": (1, 1), "6": (1, 2),
#             "1": (2, 0), "2": (2, 1), "3": (2, 2),
#             "0": (3, 1), "A": (3, 2)
#         }
#     return positions[char]
#
#
# def generate_sequence(target_code: str) -> str:
#     """Generate the sequence needed to input the target code."""
#     # For numeric keypad path
#     numeric_path = []
#     current_pos = get_position("A", "numeric")
#
#     for digit in target_code:
#         target_pos = get_position(digit, "numeric")
#         path = find_shortest_path(current_pos, target_pos, "numeric")
#         numeric_path.extend(path + ["A"])
#         current_pos = target_pos
#
#     numeric_sequence = "".join(numeric_path)
#
#     # For second robot's directional keypad
#     directional_path = []
#     current_pos = get_position("A", "directional")
#
#     for action in numeric_sequence:
#         target_pos = get_position(action, "directional")
#         path = find_shortest_path(current_pos, target_pos, "directional")
#         directional_path.extend(path + ["A"])
#         current_pos = target_pos
#
#     directional_sequence = "".join(directional_path)
#
#     # For first robot's directional keypad (your input)
#     final_path = []
#     current_pos = get_position("A", "directional")
#
#     for action in directional_sequence:
#         target_pos = get_position(action, "directional")
#         path = find_shortest_path(current_pos, target_pos, "directional")
#         final_path.extend(path + ["A"])
#         current_pos = target_pos
#
#     return "".join(final_path)
#
#
# def calculate_complexity(code: str) -> int:
#     """Calculate complexity for a given code."""
#     sequence = generate_sequence(code)
#     numeric_part = int(code[:-1])  # Remove 'A' and convert to integer
#     return len(sequence) * numeric_part
#
#
# # Calculate for all codes
# codes = ["540A", "582A", "169A", "593A", "579A"]
# total_complexity = 0
#
# for code in codes:
#     complexity = calculate_complexity(code)
#     print(
#         f"Code: {code}, Sequence length: {len(generate_sequence(code))}, Numeric part: {int(code[:-1])}, Complexity: {complexity}")
#     total_complexity += complexity
#
# print(f"\nTotal complexity: {total_complexity}")


# # Define the keypad layout and its coordinates
# keypad = {
#     '7': (0, 0), '8': (0, 1), '9': (0, 2),
#     '4': (1, 0), '5': (1, 1), '6': (1, 2),
#     '1': (2, 0), '2': (2, 1), '3': (2, 2),
#     '0': (3, 1), 'A': (3, 2),
# }
#
# # Calculate Manhattan distance between two points on the keypad
# def manhattan_distance(pos1, pos2):
#     return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
#
# # Calculate the sequence length for a given code
# def calculate_sequence_length(code):
#     current_position = keypad['A']  # Start at 'A'
#     sequence_length = 0
#
#     for char in code:
#         target_position = keypad[char]
#         sequence_length += manhattan_distance(current_position, target_position) + 1  # +1 to press
#         current_position = target_position
#
#     return sequence_length
#
# # Calculate complexity for all codes
# def calculate_complexity(codes):
#     total_complexity = 0
#
#     for code in codes:
#         numeric_part = int(code[:-1])  # Extract numeric part (ignore 'A')
#         sequence_length = calculate_sequence_length(code)
#         total_complexity += sequence_length * numeric_part
#
#     return total_complexity
#
# # Input codes
# codes = ["540A", "582A", "169A", "593A", "579A"]
#
# # Compute total complexity
# total_complexity = calculate_complexity(codes)
# print(total_complexity)


# from collections import deque
#
# # Define the keypad layout and its coordinates
# keypad = {
#     '7': (0, 0), '8': (0, 1), '9': (0, 2),
#     '4': (1, 0), '5': (1, 1), '6': (1, 2),
#     '1': (2, 0), '2': (2, 1), '3': (2, 2),
#     '0': (3, 1), 'A': (3, 2),
# }
#
# # Reverse mapping of keypad to allow coordinate lookup
# reverse_keypad = {v: k for k, v in keypad.items()}
#
# # Valid moves on the keypad
# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
#
#
# # Find shortest path between two keys using BFS
# def shortest_path(start, end):
#     start_pos = keypad[start]
#     end_pos = keypad[end]
#     queue = deque([(start_pos, 0)])  # (current_position, steps)
#     visited = set()
#     visited.add(start_pos)
#
#     while queue:
#         current, steps = queue.popleft()
#         if current == end_pos:
#             return steps + 1  # Include the press action
#
#         for d in directions:
#             neighbor = (current[0] + d[0], current[1] + d[1])
#             if neighbor in reverse_keypad and neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append((neighbor, steps + 1))
#     return float('inf')  # Should not happen
#
#
# # Calculate the sequence length for a given code
# def calculate_sequence_length(code):
#     current_key = 'A'  # Start at 'A'
#     sequence_length = 0
#
#     for char in code:
#         sequence_length += shortest_path(current_key, char)
#         current_key = char
#
#     return sequence_length
#
#
# # Calculate complexity for all codes
# def calculate_complexity(codes):
#     total_complexity = 0
#
#     for code in codes:
#         numeric_part = int(code[:-1])  # Extract numeric part (ignore 'A')
#         sequence_length = calculate_sequence_length(code)
#         total_complexity += sequence_length * numeric_part
#
#     return total_complexity
#
#
# # Input codes
# codes = ["540A", "582A", "169A", "593A", "579A"]
#
# # Compute total complexity
# total_complexity = calculate_complexity(codes)
# print(total_complexity)
# def calculate_complexity(codes):
#     # Keypad layout and transitions
#     numeric_keypad = {
#         '7': (0, 0), '8': (0, 1), '9': (0, 2),
#         '4': (1, 0), '5': (1, 1), '6': (1, 2),
#         '1': (2, 0), '2': (2, 1), '3': (2, 2),
#         '0': (3, 1), 'A': (3, 2)
#     }
#
#     def manhattan_distance(pos1, pos2):
#         return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
#
#     def sequence_length(code):
#         current_position = numeric_keypad['A']  # Start at 'A'
#         presses = 0
#
#         for char in code:
#             target_position = numeric_keypad[char]
#             presses += manhattan_distance(current_position, target_position) + 1  # Move and press
#             current_position = target_position
#
#         return presses
#
#     # Calculate complexities for each code
#     total_complexity = 0
#     for code in codes:
#         length = sequence_length(code)
#         numeric_value = int(code.strip('A'))  # Remove 'A' and convert to number
#         total_complexity += length * numeric_value
#
#     return total_complexity
#
# # Input codes
# codes = ["540A", "582A", "169A", "593A", "579A"]
#
# # Calculate and print the total complexity
# total = calculate_complexity(codes)
# print("Total Complexity:", total)


#
#
# from collections import deque
#
# def bfs_find_shortest_path(keypad, start, target):
#     directions = {
#         "^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)
#         }
#     queue = deque([(start, [])])
#     visited = set()
#
#     while queue:
#         (x, y), path = queue.popleft()
#
#         if (x, y) == target:
#             return path
#
#         if (x, y) in visited:
#             continue
#
#         visited.add((x, y))
#
#         for d, (dx, dy) in directions.items():
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < len(keypad) and 0 <= ny < len(keypad[0]) and keypad[nx][ny] != " ":
#                 queue.append(((nx, ny), path + [d]))
#
#     return []  # No path found
#
# def find_sequence(keypad, start_pos, code):
#     pos = start_pos
#     sequence = []
#
#     for char in code:
#         target = None
#         for i in range(len(keypad)):
#             for j in range(len(keypad[i])):
#                 if keypad[i][j] == char:
#                     target = (i, j)
#                     break
#             if target:
#                 break
#
#         if not target:
#             raise ValueError(f"Target {char} not found on keypad")
#
#         path = bfs_find_shortest_path(keypad, pos, target)
#         sequence.extend(path + ['A'])
#         pos = target
#
#     return sequence
#
# def calculate_complexity(sequence, code):
#     numeric_part = int(''.join(filter(str.isdigit, code)))
#     return len(sequence) * numeric_part
#
# if __name__ == "__main__":
#     keypad = [
#         ["7", "8", "9"],
#         ["4", "5", "6"],
#         ["1", "2", "3"],
#         [" ", "0", "A"]
#     ]
#
#     start_position = (3, 2)  # Starting at 'A'
#     codes = ["029A", "980A", "179A", "456A", "379A"]
#
#     total_complexity = 0
#
#     for code in codes:
#         sequence = find_sequence(keypad, start_position, code)
#         complexity = calculate_complexity(sequence, code)
#         total_complexity += complexity
#         print(f"Code: {code}, Sequence: {''.join(sequence)}, Complexity: {complexity}")
#
#     print(f"Total Complexity: {total_complexity}")


import Day0 as AoC
from collections import Counter

def get_step_count(G: dict[complex, str], s: str, i=1):
    px, py = G["A"]
    bx, by = G[" "]
    count = Counter()
    for c in s:
        npx, npy = G[c]
        f = (npx == bx and py == by) or (npy == by and px == bx)
        count[(npx - px, npy - py, f)] += i
        px, py = npx, npy
    return count

def solve(depth):
    score = 0
    for code in Lines:
        steps = get_step_count(keypad, code)
        for _ in range(depth):
            steps = sum((get_step_count(dirpad, ("<" * -x + "v" * y + "^" * -y + ">" * x)[:: -1 if f else 1] + "A", steps[(x, y, f)]) for x, y, f in steps), Counter())
        score += steps.total() * int(code[:3])
    return score

Lines = AoC.Init("input.txt")[0]
keypad = {c: (i % 3, i // 3) for i, c in enumerate("789456123 0A")}
dirpad = {c: (i % 3, i // 3) for i, c in enumerate(" ^A<v>")}
AoC.verify(177814, 220493992841852)
AoC.run(solve(3), solve(26))