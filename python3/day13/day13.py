import math

INPUT = open("input.txt").read()
TIMESTAMP, sched = INPUT.splitlines()
TIMESTAMP = int(TIMESTAMP)
BUSES = [int(bus) for bus in sched.split(",") if bus != "x"]
FULL_BUS_LIST = [int(b) if b != "x" else None for b in sched.split(",")][::-1]


def part1():
    departures = [bus * math.ceil(TIMESTAMP / bus) for bus in BUSES]
    bus, departure = min(zip(BUSES, departures), key=lambda schedule: schedule[1])
    return bus * (departure - TIMESTAMP)


def find_bus_cadence(a, b, start, offset):
    n = start
    while (n - offset) % a != 0:
        n += b
    m = n + b
    while (m - offset) % a != 0:
        m += b
    return n, m - n


def part2():
    offset = 0
    cadence = FULL_BUS_LIST[0]
    answer = FULL_BUS_LIST[0]
    for bus in FULL_BUS_LIST[1:]:
        offset += 1
        if bus is None:
            continue
        answer, cadence = find_bus_cadence(bus, cadence, answer, offset)
    answer -= offset
    return answer


print(part1())
print(part2())