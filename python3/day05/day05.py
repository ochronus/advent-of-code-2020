from string import maketrans


lines = open("input.txt").read().split()
TRANSLATION_TABLE = maketrans("FBLR", "0101")
SEAT_IDS = []


def get_seat_id(instructions):
    return int(instructions.translate(TRANSLATION_TABLE), 2)


def part1():
    max = 0
    for line in lines:
        id = get_seat_id(line)
        SEAT_IDS.append(id)
        if id > max:
            max = id

    return max


def part2():
    SEAT_IDS.sort()
    for (i, n) in enumerate(SEAT_IDS):
        if SEAT_IDS[i + 1] != n + 1:
            return n + 1


print(part1())
print(part2())
