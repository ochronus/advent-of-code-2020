adapter_list = [0] + [int(x) for x in open("input.txt").read().split()]
adapter_list += [max(adapter_list) + 3]
adapter_list.sort()
adapter_count = len(adapter_list)


def part1():
    jolt1 = [
        "x"
        for i in range(1, adapter_count)
        if adapter_list[i] - adapter_list[i - 1] == 1
    ]

    jolt3 = [
        "x"
        for i in range(1, adapter_count)
        if adapter_list[i] - adapter_list[i - 1] == 3
    ]

    return len(jolt1) * len(jolt3)


def part2():
    counts = [1] + [0] * (adapter_count - 1)
    for i in range(1, adapter_count):
        for j in range(0, i):
            if (adapter_list[i] - adapter_list[j]) in [1, 2, 3]:
                counts[i] += counts[j]

    return counts[-1]


print(part1())
print(part2())
