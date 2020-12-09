numbers = [int(l) for l in open("input.txt").readlines()]


def part1():
    for i in range(25, len(numbers)):
        sliding_window = numbers[(i - 25) : i]

        found_two_numbers = False
        for j in range(25):
            for k in range(25):
                if (j != k) and (sliding_window[j] + sliding_window[k] == numbers[i]):
                    found_two_numbers = True
                    break

        if not found_two_numbers:
            return numbers[i], i


def part2(outlier, pos):
    for i in range(pos - 2):
        for j in range(i + 2, pos):
            slice = numbers[i:j]
            if sum(slice) == outlier:
                return min(slice) + max(slice)


outlier, pos = part1()
print(outlier)
print(part2(outlier, pos))
