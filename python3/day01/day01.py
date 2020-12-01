import itertools

numList = [int(x) for x in open("input.txt").read().split()]


print([a * b for (a, b) in itertools.combinations(numList, 2) if a + b == 2020][0])
print(
    [
        a * b * c
        for (a, b, c) in itertools.combinations(numList, 3)
        if a + b + c == 2020
    ][0]
)
