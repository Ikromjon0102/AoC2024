def checksum_1(file_map: str) -> int:
    res = 0
    expanded = []
    for i, c in enumerate(file_map):
        expanded += [i // 2 if i % 2 == 0 else None] * int(c)

    l, r = 0, len(expanded) - 1
    while l <= r:
        if expanded[l] is None:
            while expanded[r] is None:
                r -= 1
            if r < l:
                break
            res += l * expanded[r]
            r -= 1
        else:
            res += l * expanded[l]
        l += 1
    return res


def checksum_2(file_map: str) -> int:
    res = 0
    moved = set()
    filled = {}
    free_space = {i: int(file_map[i]) for i in range(1, len(file_map), 2)}
    for i in range(len(file_map) - 1, -1, -1):
        if i % 2 != 0:
            continue

        sz = int(file_map[i])
        new_idx = min(
            (j for j in range(1, i, 2) if free_space[j] >= sz),
            default=None,
        )
        if new_idx is not None:
            moved.add(i)
            free_space[new_idx] -= sz
            if new_idx not in filled:
                filled[new_idx] = []
            filled[new_idx] += [i // 2] * sz

    ptr = 0
    for i in range(len(file_map)):
        sz = int(file_map[i])
        if i in moved:
            ptr += sz
            continue
        if i % 2 == 0:
            res += (i // 2) * sz * (ptr + (sz - 1) / 2)
            ptr += sz
        else:
            start = ptr
            for v in filled.get(i, []):
                res += start * v
                start += 1

            ptr += sz

    return int(res)


if __name__ == "__main__":
    filename = 'input.txt'
    with open(filename, "r") as f:
        file_map = f.read().strip()

    print(checksum_1(file_map))
    print(checksum_2(file_map))