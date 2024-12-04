import os

def get_input() -> list[list[str]]:
    data_file_path = os.path.join(os.path.dirname(__file__), "../data/day_4.txt")
    with open(data_file_path, "r") as fp:
        return [[c for c in line.replace("\n", "")] for line in fp.readlines()]
    

def _part_1(grid: list[list], pos_x: int, pos_y: int) -> int:
    instances_of_xmas = 0
    for inc_y in range(-1, 2):
        for inc_x in range(-1, 2):
            if inc_x == 0 and inc_y == 0:
                continue

            increment_instances = True
            try:
                for i, c in enumerate(["M", "A", "S"]):
                    check_y = pos_y + ((i + 1) * inc_y)
                    check_x = pos_x + ((i + 1) * inc_x)

                    if check_x < 0 or check_y < 0:
                        raise IndexError
                    
                    if check_y > len(grid) or check_x > len(grid[0]):
                        raise IndexError

                    if grid[check_y][check_x] != c:
                        increment_instances = False
                        break
                
                instances_of_xmas += 1 if increment_instances else 0
            
            except IndexError:
                continue
    
    return instances_of_xmas
    

def _part_2(grid: list[list], pos_x: int, pos_y: int) -> int:
    to_find = ["M", "M", "S", "S"]
    for inc_y in range(-1, 2):
        for inc_x in range(-1, 2):
            if inc_x == 0 or inc_y == 0:
                continue

            try:
                check_y = pos_y + inc_y
                check_x = pos_x + inc_x

                if check_x < 0 or check_y < 0:
                    raise IndexError
                
                if check_y > len(grid) or check_x > len(grid[0]):
                    raise IndexError
                
                # There needs to be 2 Ms and 2s
                to_find.remove(grid[check_y][check_x])

                # If the opposite diagonals are the same char then it fails
                # Example of bad permutation
                # . M . S
                # . . A .
                # . S . M
                opposite_y = pos_y + (inc_y * -1)
                opposite_x = pos_x + (inc_x * -1)

                if opposite_x < 0 or opposite_y < 0:
                    raise IndexError

                if opposite_y > len(grid) or opposite_x > len(grid[0]):
                    raise IndexError
                
                if grid[check_y][check_x] == grid[opposite_y][opposite_x]:
                    raise ValueError

            
            except IndexError:
                return 0
            except ValueError:
                return 0
    
    return 0 if to_find else 1


def part_1(puzzle: list[list[str]]) -> int:
    answer = 0

    for y, row in enumerate(puzzle):
        for x, c in enumerate(row):
            if c == "X":
                # Check all 8 directions
                answer += _part_1(puzzle, x, y)

    return answer


def part_2(puzzle: list[list[str]]) -> int:
    answer = 0

    for y, row in enumerate(puzzle):
        for x, c in enumerate(row):
            if c == "A":
                # Check all 8 directions
                answer += _part_2(puzzle, x, y)

    return answer


if __name__ == "__main__":
    _input = get_input()
    print(f"Day 4 Part 1: {part_1(_input)}")
    print(f"Day 4 Part 2: {part_2(_input)}")