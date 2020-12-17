import re


PROGRAM = open("input.txt").readlines()
MASK = r"mask = ([X10]+)"
MEMORY = r"mem\[(\d+)\] = (\d+)"


def create_bitmasks(mask):
    masks = []
    count = mask.count("X")
    for value in range(2 ** count):
        binary = bin(value)[2:].zfill(count)
        newmask = re.sub("[01]", "PLACEHOLDER", mask)
        for digit in binary:
            newmask = newmask.replace("X", digit, 1)
        zeroes = int(re.sub("PLACEHOLDER", "1", newmask), 2)
        ones = int(re.sub("PLACEHOLDER", "0", newmask), 2)
        masks.append((zeroes, ones))
    return masks


def both_parts():
    ones = 0
    zeroes = 2 ** 35
    memory_part1 = {}
    memory_part2 = {}
    bitmasks = []
    for line in PROGRAM:
        mask = re.findall(MASK, line)
        if mask:
            zeroes = int(re.sub("X", "1", mask[0]), 2)
            ones = int(re.sub("X", "0", mask[0]), 2)
            bitmasks = create_bitmasks(mask[0])
        else:
            match = re.findall(MEMORY, line)
            if match:
                addr, value = map(int, match[0])
                memory_part1[addr] = (value & zeroes) | ones
                for mask in bitmasks:
                    target_addr = ((addr | ones) & mask[0]) | mask[1]
                    memory_part2[target_addr] = value

    return (sum(memory_part1.values()), sum(memory_part2.values()))


print(both_parts())
