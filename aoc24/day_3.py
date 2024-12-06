import os
import re


def get_input() -> list[str]:
    data_file_path = os.path.join(os.path.dirname(__file__), "../data/day_3.txt")
    with open(data_file_path, "r") as fp:
        return [line.replace("\n", "") for line in fp.readlines()]


def part_1(instructions: list[str]) -> int:
    answer = 0
    pattern = r"mul\(\d+,\d+\)"

    for instruction in instructions:
        matches = re.findall(pattern, instruction)
        for match in matches:
            numbers = match[4:-1].split(",")
            answer += int(numbers[0]) * int(numbers[1])

    return answer


def _get_match_type(match: tuple[str, str, str]) -> str:
    if match[0] != "":
        return "MUL"
    if match[1] != "":
        return "DO"
    if match[2] != "":
        return "DON'T"

    raise NotImplementedError(f"Unknown Match {match}")


def part_2(instructions: list[str]) -> int:
    answer = 0
    enabled = True
    pattern = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"

    for instruction in instructions:
        matches = re.findall(pattern, instruction)
        for match in matches:
            match_type = _get_match_type(match)

            if match_type == "MUL":
                if enabled:
                    numbers = match[0][4:-1].split(",")
                    answer += int(numbers[0]) * int(numbers[1])
            else:
                enabled = match_type == "DO"

    return answer


if __name__ == "__main__":
    _input = get_input()
    print(f"Day 3 Part 1: {part_1(_input)}")
    print(f"Day 3 Part 2: {part_2(_input)}")
