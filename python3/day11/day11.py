from copy import deepcopy

SEATING_MAP = [list(l.strip()) for l in open("input.txt").readlines()]
ROWS = len(SEATING_MAP)
COLUMNS = len(SEATING_MAP[0])
NEIGHBOURHOOD = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def get_neighbor(row, col, dc, dr, seating_map, is_part2):
    neighbor_row = row + dr
    neighbor_col = col + dc
    if not (0 <= neighbor_row < ROWS and 0 <= neighbor_col < COLUMNS):
        return None

    if not is_part2 and (0 <= neighbor_row < ROWS and 0 <= neighbor_col < COLUMNS):
        return seating_map[neighbor_row][neighbor_col]

    if is_part2:
        while seating_map[neighbor_row][neighbor_col] == ".":
            neighbor_row = neighbor_row + dr
            neighbor_col = neighbor_col + dc
            if not (0 <= neighbor_row < ROWS and 0 <= neighbor_col < COLUMNS):
                return None

        return seating_map[neighbor_row][neighbor_col]

    return None


def solve(is_part2):
    current_seating_map = deepcopy(SEATING_MAP)
    threshold = 5 if is_part2 else 4
    while True:
        new_seating_map = deepcopy(current_seating_map)
        no_change = True
        for row in range(ROWS):
            for col in range(COLUMNS):
                occupied_neighbors = 0
                for dr, dc in NEIGHBOURHOOD:
                    neighbor = get_neighbor(
                        row, col, dr, dc, current_seating_map, is_part2
                    )
                    if not neighbor:
                        continue

                    if neighbor == "#":
                        occupied_neighbors += 1

                if current_seating_map[row][col] == "L":
                    if occupied_neighbors == 0:
                        new_seating_map[row][col] = "#"
                        no_change = False
                elif (
                    current_seating_map[row][col] == "#"
                    and occupied_neighbors >= threshold
                ):
                    new_seating_map[row][col] = "L"
                    no_change = False

        if no_change:
            break

        current_seating_map = deepcopy(new_seating_map)

    return len([x for row in current_seating_map for x in row if x == "#"])


print(solve(True))
print(solve(False))
