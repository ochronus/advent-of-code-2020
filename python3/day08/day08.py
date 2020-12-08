from copy import deepcopy


original_program = [l.split() for l in open("input.txt").readlines()]
program_length = len(original_program)


def execute_instruction(program, ip, acc):
    instruction, operand = program[ip]

    if instruction == "acc":
        acc += int(operand)
        ip += 1

    elif instruction == "jmp":
        ip += int(operand)

    elif instruction == "nop":
        ip += 1

    return (ip, acc)


def run_program(program):
    ip = 0
    acc = 0
    already_executed = []
    while True:
        if ip in already_executed or ip == program_length:
            return ip, acc

        already_executed.append(ip)
        ip, acc = execute_instruction(program, ip, acc)


def part1():
    _, acc = run_program(original_program)
    return acc


def part2():
    for ip_to_change in range(program_length):
        if original_program[ip_to_change][0] == "jmp":
            modified_program = deepcopy(original_program)
            modified_program[ip_to_change][0] = "nop"
        elif (
            original_program[ip_to_change][0] == "nop"
            and original_program[ip_to_change][1] != "0"
        ):
            modified_program = deepcopy(original_program)
            modified_program[ip_to_change][0] = "jmp"
        else:
            continue

        ip, acc = run_program(modified_program)
        if ip == program_length:
            return acc


print(part1())
print(part2())
