from collections import defaultdict, deque

input = [1, 0, 15, 2, 10, 13]
PART1 = 2020
PART2 = 30000000

already_spoken = defaultdict(lambda: deque([], maxlen=2))
last = input[-1]

for i in range(1, len(input) + 1):
    already_spoken[input[i - 1]].append(i)

for j in range(i + 1, PART2 + 1):
    if len(already_spoken[last]) < 2:
        last = 0
    else:
        last = already_spoken[last][-1] - already_spoken[last][-2]
    already_spoken[last].append(j)
    if j == PART1:
        print("Part 1:", last)

print("Part 2:", last)
