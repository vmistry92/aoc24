import os

from collections import defaultdict


"""
    Grid syntax:

     X        0    1
  Y  -------->
    |    [
  0 |       [".", ".", ".",".","#",".",".",".",".","."],
  1 |       [".", ".", ".",".",".",".",".",".",".","#"],
    |       [".", ".", ".",".",".",".",".",".",".","."],
    |       [".", ".", "#",".",".",".",".",".",".","."],
    V       [".", ".", ".",".",".",".",".","#",".","."],
            [".", ".", ".",".",".",".",".",".",".","."],
            [".", "#", ".",".","^",".",".",".",".","."],
            [".", ".", ".",".",".",".",".",".","#","."],
            ["#", ".", ".",".",".",".",".",".",".","."],
            [".", ".", ".",".",".",".","#",".",".","."],
        ]

    Coordinates: (X, Y)
    Headings are increments to X and Y coordinates:
        + UP: (0, -1)  # UP or ^ in this specific example

    Access the grid with the tuple of coordinates: 
        + grid[Y][X] 
        + grid[coordinates[1]][coordinates[0]]

"""

UP = (0, -1)  # ^
RIGHT = (1, 0)  # >
DOWN = (0, 1)  # V
LEFT = (-1, 0)  # <

CHAR_DIRECTION_MAP = {
    "^": UP,
    ">": RIGHT,
    "V": DOWN,
    "<": LEFT,
}


def get_input() -> list[list[str]]:
    data_file_path = os.path.join(os.path.dirname(__file__), "../data/day_6.txt")
    with open(data_file_path, "r") as fp:
        return [[c for c in line.replace("\n", "")] for line in fp.readlines()]
    

def scan_grid(lab_map: list[list[str]]) -> tuple[tuple, tuple, set]:
    position = (-1, -1)
    heading = (0, 0)
    obstacles = set()

    for y, row in enumerate(lab_map):
        for x, c in enumerate(row):
            if c == ".":
                continue
            if c == "#":
                obstacles.add((x, y))
                continue
            if c in CHAR_DIRECTION_MAP:
                position = (x, y)
                heading = CHAR_DIRECTION_MAP[c]

    return position, heading, obstacles


def is_in_bounds(lab_map: list[list[str]], position: tuple[int, int]) -> bool:
    if position[0] < 0 or position[1] < 0:
        return False
    
    max_y = len(lab_map) - 1
    max_x = len(lab_map[0]) - 1

    if position[0] > max_x or position[1] > max_y:
        return False

    return True


def part_1(lab_map: list[list[str]]) -> dict[tuple[int, int], set]:
    in_bounds = True
    positions_and_headings = defaultdict(set)
    position, heading, obstacles = scan_grid(lab_map)

    while in_bounds:
        positions_and_headings[position].add(heading)
        next_position = (position[0] + heading[0], position[1] + heading[1])

        if next_position in obstacles:
            heading = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}[heading]
            continue
        
        in_bounds = is_in_bounds(lab_map, next_position)
        position = next_position

    return positions_and_headings


def detect_cycle(positions_and_headings: dict[tuple[int, int], set[tuple[int, int]]], position: tuple[int, int], heading: tuple[int, int]) -> bool:
    # How do you find a cycle: if you have visited the position before in the same heading that would be a cycle
    return heading in positions_and_headings.get(position, set())


def part_2(lab_map: list[list[str]], positions_visited: list[tuple[int, int]]) -> int:
    answer = 0
    initial_position, initial_heading, obstacles = scan_grid(lab_map)
    
    # How many times along the path you have already walked if you placed an obstacle would it result in a cycle?
    for i, candidate_obstacle_position in enumerate(positions_visited):
        if candidate_obstacle_position == initial_position:
            # Cannot place an obstacle on the starting location
            continue    
        
        print(f"Evaluating: {i} of {len(positions_visited)} candidates")
        obstacles_with_candidate = obstacles.copy()
        obstacles_with_candidate.add(candidate_obstacle_position)

        in_bounds = True
        has_cycle = False
        heading = initial_heading
        position = initial_position
        positions_and_headings = defaultdict(set)

        while in_bounds and not has_cycle:
            positions_and_headings[position].add(heading)
            next_position = (position[0] + heading[0], position[1] + heading[1])

            if next_position in obstacles_with_candidate:
                heading = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}[heading]
                continue
            
            in_bounds = is_in_bounds(lab_map, next_position)
            has_cycle = detect_cycle(positions_and_headings, next_position, heading)
            position = next_position

        answer += 1 if has_cycle else 0
        
    return answer


if __name__ == "__main__":
    _lab_map = get_input()
    _positions_and_headings = part_1(_lab_map)
    print(f"Day 6 Part 1: {len(_positions_and_headings)}")
    print(f"Day 6 Part 2: {part_2(_lab_map, list(_positions_and_headings.keys()))}")
