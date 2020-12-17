input = open("input.txt").readlines()

fields_input = input[:20]
your_ticket = [int(x) for x in input[22].split(",")]
other_tickets = [[int(x) for x in line.split(",")] for line in input[25:]]


fields = {}
valid_tickets = []


def parse_fields():
    for field in fields_input:
        name, rest = field.split(": ")
        range1, range2 = rest.split(" or ")
        start1, end1 = range1.split("-")
        start2, end2 = range2.split("-")
        fields[name] = [(int(start1), int(end1)), (int(start2), int(end2))]


def part1():
    error_rate = 0
    for ticket in other_tickets:
        all_fields_valid = True

        for value in ticket:
            has_valid_field = False
            for _, ranges in fields.items():
                for min, max in ranges:
                    if min <= value and value <= max:
                        has_valid_field = True
                        break
                if has_valid_field:
                    break

            if not has_valid_field:
                error_rate += value
                all_fields_valid = False

        if all_fields_valid:
            valid_tickets.append(ticket)
    return error_rate


def part2():
    field_options = [set(fields.keys()) for _ in your_ticket]

    for ticket in valid_tickets:
        for i in range(len(ticket)):
            value = ticket[i]
            for field, ranges in fields.items():
                ok = False
                for start, end in ranges:
                    if start <= value and value <= end:
                        ok = True
                        break
                if not ok:
                    field_options[i].remove(field)

    for _ in range(len(field_options)):
        for i in range(len(field_options)):
            if len(field_options[i]) == 1:
                for j in range(len(field_options)):
                    if j != i:
                        field_options[j] -= field_options[i]
    result = 1

    for i in range(len(your_ticket)):
        for field_option in field_options[i]:
            if field_option[:9] == "departure":
                result *= your_ticket[i]

    return result


parse_fields()
print(part1())
print(part2())
