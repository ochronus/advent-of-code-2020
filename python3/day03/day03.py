AREA_MAP = open("input.txt").read().split()


def travel_and_count(right, down):
    height, width = len(AREA_MAP), len(AREA_MAP[0])
    tree_count = 0

    x = 0
    for y in range(0, height, down):
        tree_count += AREA_MAP[y][x] == "#"
        x = (x + right) % width

    return tree_count


def part1():
    return travel_and_count(3, 1)


def part2():
    tree_count = 1
    travel_patterns = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for pattern in travel_patterns:
        tree_count *= travel_and_count(pattern[0], pattern[1])
    return tree_count


print(part1())
print(part2())