import re


REQUIRED_FIELDS = set(["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"])
EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

lines = [x.rstrip("\n") for x in open("input.txt").read().split("\n\n")]


def part1():
    valid_passports = 0

    for line in lines:
        fields = re.findall(r"(\w+):", line)
        if len(REQUIRED_FIELDS - set(fields)) == 0:
            valid_passports += 1

    return valid_passports


def validate_field(key, val):
    field_valid = False
    if key == "byr":
        field_valid = 1920 <= int(val) <= 2002
    elif key == "iyr":
        field_valid = 2010 <= int(val) <= 2020
    elif key == "eyr":
        field_valid = 2020 <= int(val) <= 2030
    elif key == "hgt":
        if val.endswith("cm"):
            field_valid = 150 <= int(val[:-2]) <= 193
        elif val.endswith("in"):
            field_valid = 59 <= int(val[:-2]) <= 76
    elif key == "hcl":
        field_valid = re.fullmatch(r"#[0-9a-f]{6}", val) != None
    elif key == "ecl":
        field_valid = val in EYE_COLORS
    elif key == "pid":
        field_valid = re.fullmatch(r"[0-9]{9}", val) != None
    else:
        field_valid = True

    return field_valid


def part2():
    valid_passports = 0
    for line in lines:
        fields_keyvals = re.findall(r"(\w+):(\S+)", line)
        keys = set(x[0] for x in fields_keyvals)

        if len(REQUIRED_FIELDS - keys) > 0:
            continue

        passport_valid = False
        for key, val in fields_keyvals:
            passport_valid = validate_field(key, val)
            if not passport_valid:
                break

        if passport_valid:
            valid_passports += 1

    return valid_passports


print(part1())
print(part2())
