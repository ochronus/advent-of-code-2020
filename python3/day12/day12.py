action_list = [
    (chars[0], int("".join(chars[1:]))) for chars in open("input.txt").readlines()
]


def part1():
    direction = 1
    vector = 0
    for action, amount in action_list:
        if action == "F":
            vector += direction * amount
        elif action == "E":
            vector += amount
        elif action == "W":
            vector -= amount
        elif action == "N":
            vector += amount * 1j
        elif action == "S":
            vector -= amount * 1j
        elif action == "L":
            direction *= 1j ** (amount // 90)
        elif action == "R":
            direction /= 1j ** (amount // 90)

    return abs(vector.real) + abs(vector.imag)


def part2():
    vector = 0
    waypoint = 10 + 1j
    for action, amount in action_list:
        if action == "F":
            vector += amount * waypoint
        elif action == "E":
            waypoint += amount
        elif action == "W":
            waypoint -= amount
        elif action == "N":
            waypoint += amount * 1j
        elif action == "S":
            waypoint -= amount * 1j
        elif action == "L":
            waypoint *= 1j ** (amount // 90)
        elif action == "R":
            waypoint /= 1j ** (amount // 90)

    return abs(vector.real) + abs(vector.imag)


print(part1())
print(part2())
