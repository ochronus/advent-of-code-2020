answers_groups = open("input.txt").read().split("\n\n")


def part1():
    return sum(len(set(group.replace("\n", ""))) for group in answers_groups)


def part2():
    # OK this one looks weird I admit.
    # we create a set from each line (== each person's anwers) with map(set, ...), e.g. {'d', 'w', 't', 'b'}
    # *map unpacks the value of the map object to a list of sets
    # then we want to know the intersection of all person's answers in the group
    return sum(
        len(set.intersection(*map(set, group.splitlines()))) for group in answers_groups
    )


print(part1())
print(part2())
