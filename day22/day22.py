# from functools import lru_cache
# from os import path
#
# ROOT_DIR = path.dirname(__file__)
#
#
# def get_data(filename="input.txt"):
#     full_name = path.join(ROOT_DIR, filename)
#     with open(full_name) as f:
#         return f.read().splitlines()
#
#
# def parse_data(data):
#     return [int(x) for x in data]
#
#
# @lru_cache(maxsize=None)
# def mix(secret: int, val: int) -> int:
#     """
#     To mix a value into the secret number, calculate the bitwise XOR of the given value and
#     the secret number. Then, the secret number becomes the result of that operation.
#     """
#     return secret ^ val
#
#
# @lru_cache(maxsize=None)
# def prune(secret: int) -> int:
#     """
#     To prune the secret number, calculate the value of the secret number modulo 16777216.
#     Then, the secret number becomes the result of that operation.
#     """
#     return secret % 2**24
#
#
# @lru_cache(maxsize=None)
# def calculate_secret(secret):
#     """
#     In particular, each buyer's secret number evolves into the next secret number in the sequence via the
#     following process:
#
#     Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret
#     number. Finally, prune the secret number.
#
#     Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
#     Then, mix this result into the secret number. Finally, prune the secret number.
#
#     Calculate the result of multiplying the secret number by 2048. Then, mix this result into the
#     secret number. Finally, prune the secret number.
#     """
#     val = secret * 2**6
#     secret = prune(mix(secret, val))
#     val = secret // 2**5
#     secret = prune(mix(secret, val))
#     val = secret * 2**11
#     secret = prune(mix(secret, val))
#     return secret
#
#
# def calculate_secret_n(secret, n):
#     """
#     Calculate the secret number after n iterations
#     """
#     for _ in range(n):
#         secret = calculate_secret(secret)
#     return secret
#
#
# def calculate_price_diff_n(secret, n):
#     """
#     Calculate the secret number after n iterations
#     """
#     prev_price = None
#     for _ in range(n):
#         secret = calculate_secret(secret)
#         curr_price = secret % 10
#         if prev_price is None:
#             curr_diff = None
#         else:
#             curr_diff = curr_price - prev_price
#         yield (curr_price, curr_diff)
#         prev_price = curr_price
#
#
# def part1(data):
#     """Part 1"""
#     initials = parse_data(data)
#     total = 0
#     for x in initials:
#         result = calculate_secret_n(x, 2000)
#         # print(f"{x}: {result}")
#         total += result
#     return total
#
#
# def part2(data):
#     """Part 2"""
#     initials = parse_data(data)
#     for x in initials:
#         diffs = calculate_price_diff_n(x, 100)
#         for i, (diff, price) in enumerate(diffs):
#             print(f"{i}: {diff}, {price}")
#         break
#     return 0
#
#
# if __name__ == "__main__":
#     print(f"Part 1: {part1(get_data('input.txt'))}")
#     print(f"Part 2: {part2(get_data('example.txt'))}")

from itertools import pairwise
from collections import defaultdict

secret_numbers = []

with open("input.txt", "r") as file:
    for line in file:
        secret_numbers.append(int(line.strip()))


def get_next_secret_number(secret_number):
    step_one = (secret_number ^ (secret_number * 64)) % 16777216
    step_two = (step_one ^ (step_one // 32)) % 16777216
    step_three = (step_two ^ (step_two * 2048)) % 16777216

    return step_three


bananas = defaultdict(int)
numbers = []
for secret_number in secret_numbers:
    numbers = [secret_number] + [secret_number := get_next_secret_number(secret_number) for _ in range(2000)]
    diffs = [b % 10 - a % 10 for a, b in pairwise(numbers)]

    visited = set()
    for i in range(len(diffs) - 3):
        pattern = tuple(diffs[i:i + 4])
        if pattern not in visited:
            bananas[pattern] += numbers[i + 4] % 10
            visited.add(pattern)

print(max(bananas.values()))