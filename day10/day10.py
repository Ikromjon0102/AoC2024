def load_input():
    with open("input.txt", "r", encoding="utf-8") as f:
        return ['0', '37551', '469', '63', '1', '791606', '2065', '9983586']


# def main():
#     stones = load_input()
#     for _ in range(25):
#         new_stones = []
#         for stone in stones:
#             if stone == "0":
#                 new_stones.append("1")
#             elif len(stone) % 2 == 0:
#                 new_stones.append(stone[: len(stone) // 2])
#                 new_stones.append(str(int(stone[len(stone) // 2 :])))
#             else:
#                 new_stones.append(str(int(stone) * 2024))
#         stones = new_stones
#     print(len(stones))

def _stones_for(stone, remaining_steps, memo):
    if (stone, remaining_steps) in memo:
        return memo[(stone, remaining_steps)]

    stones = None
    if remaining_steps == 0:
        return 1

    if stone == "0":
        stones = _stones_for("1", remaining_steps - 1, memo)
    elif len(stone) % 2 == 0:
        stones = 0
        stones += _stones_for(stone[: len(stone) // 2], remaining_steps - 1, memo)
        stones += _stones_for(
            str(int(stone[len(stone) // 2 :])), remaining_steps - 1, memo
        )
    else:
        stones = _stones_for(str(int(stone) * 2024), remaining_steps - 1, memo)

    memo[(stone, remaining_steps)] = stones
    return stones


def main():
    stones = load_input()
    memo = {}
    stones = sum(_stones_for(stone, 75, memo) for stone in stones)
    print(stones)


if __name__ == "__main__":
    main()
