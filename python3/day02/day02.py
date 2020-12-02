import re


def parse_line(line):
    m = re.search("(\d+)-(\d+) (\w+): (\w+)", line)
    low = int(m.group(1))
    high = int(m.group(2))
    char = m.group(3)
    pw = m.group(4)
    return (low, high, char, pw)


def part1():
    counter = 0
    for line in open("input.txt").read().split("\n"):
        low, high, char, pw = parse_line(line)
        cnt = pw.count(char)
        if cnt <= high and cnt >= low:
            counter += 1
    return counter


def part2():
    counter = 0
    for line in open("input.txt").read().split("\n"):
        low, high, char, pw = parse_line(line)
        if (pw[low - 1] == char) ^ (pw[high - 1] == char):
            counter += 1
    return counter


print(part1())
print(part2())
