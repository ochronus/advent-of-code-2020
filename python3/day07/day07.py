import collections
import re

lines = [l.rstrip("\n") for l in open("input.txt").read().splitlines()]
TARGET = "shiny gold"
contained_in = collections.defaultdict(set)
contains = collections.defaultdict(list)


def parse_input():
    for line in lines:
        # plaid green bags contain 2 wavy red bags, 1 pale yellow bag, 5 posh black bags.
        container_color = re.match(r"([a-z ]+) bags c", line)[1]
        for bag_count, contained_color in re.findall(
            r"(\d+) ([a-z ]+) bags?[,.]", line
        ):
            bag_count = int(bag_count)
            contained_in[contained_color].add(container_color)
            contains[container_color].append((bag_count, contained_color))


def check_if_can_contain(target):
    for color in contained_in[target]:
        yield (color)
        yield from check_if_can_contain(color)


def part1():
    can_contain_target = set()

    for color in check_if_can_contain(TARGET):
        can_contain_target.add(color)
    return len(can_contain_target)


def calculate_bag_cost(color):
    total_cost = 0
    for (bag_count, contained_bag_color) in contains[color]:
        contained_bags_cost = calculate_bag_cost(contained_bag_color)
        total_cost += bag_count * (
            1 + contained_bags_cost
        )  # current bag plus contained bags
    return total_cost


def part2():
    return calculate_bag_cost(TARGET)


parse_input()

print(part1())
print(part2())
