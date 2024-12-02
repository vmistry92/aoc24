import os


def get_input() -> list[list[int]]:
    rows = []
    data_file_path = os.path.join(os.path.dirname(__file__), "../data/day_2.txt")
    with open(data_file_path, "r") as fp:
        for line in fp.readlines():
            rows.append([int(x) for x in line.split(" ")])

    return rows


def _get_direction_and_magnitude(current: int, next: int) -> tuple[int, int]:
    difference = current - next
    magnitude = abs(difference)
    if difference == 0:
        return 0, 0
    
    direction = 1 if difference < 0 else -1
    return direction, magnitude


def _is_safe_row(row: list[int]) -> bool:
    first_direction = 0

    for i, (current, next) in enumerate(zip(row[:-1], row[1:])):
        direction, magnitude = _get_direction_and_magnitude(current, next)

        if i == 0:
            first_direction = direction

        if magnitude > 3 or magnitude < 1:
            return False
        
        if first_direction != direction:
            return False

    return True


def part_1(_input: list[list[int]]) -> int:
    safe_row_count = 0

    for row in _input:
        safe_row_count += 1 if _is_safe_row(row) else 0

    return safe_row_count


def part_2(_input: list[list[int]]) -> int:
    safe_row_count = 0

    for row in _input:
        safe_row = _is_safe_row(row)
        if safe_row:
            safe_row_count += 1
            continue
        
        for i, _ in enumerate(row):
            to_test = row.copy()
            to_test.pop(i)
            safe_row = _is_safe_row(to_test)
            
            if safe_row:
                safe_row_count += 1
                break

    return safe_row_count


if __name__ == "__main__":
    _input = get_input()
    print(f"Day 2 Part 1: {part_1(_input)}")
    print(f"Day 2 Part 2: {part_2(_input)}")
