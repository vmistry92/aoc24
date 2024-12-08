import os
from functools import lru_cache


def get_input() -> list[str]:
    data_file_path = os.path.join(os.path.dirname(__file__), "../data/day_7.txt")
    with open(data_file_path, "r") as fp:
        return [line.replace("\n", "") for line in fp.readlines()]


def _parse_equation(equation: str) -> tuple[int, list[int]]:
    _equation = equation.split(": ")
    return (int(_equation[0]), [int(x) for x in _equation[1].split(" ")])


@lru_cache
def _get_permutations(size: int, operators: tuple[str]) -> list[str]:
    permutations = list(operators)

    for i in range(size - 2):
        new_permutations = []
        for operator in operators:
            for permutation in permutations:
                new_permutations.append(f"{permutation}{operator}")
        permutations = new_permutations

    return permutations


def _evaluate_numbers(test_value: int, numbers: list[int], operators: tuple[str]) -> bool:
    operator_permutations = _get_permutations(len(numbers), operators)

    for operator_permutation in operator_permutations:
        value = numbers[0]
        for operator, number in zip(operator_permutation, numbers[1:]):
            if operator == "*":
                value *= number
            elif operator == "+":
                value += number
            elif operator == "|":
                value = int(f"{value}{number}")
            else:
                raise ValueError()

        if value == test_value:
            return True

    return False


def _implementation(equations: list[list[int]], operators: tuple[str]) -> int:
    answer = 0

    for equation in equations:
        test_value, numbers = _parse_equation(equation)
        answer += test_value if _evaluate_numbers(test_value, numbers, operators) else 0

    return answer


def part_1(equations: list[list[int]]) -> int:
    return _implementation(equations, ("*", "+"))


def part_2(equations: list[list[int]]) -> int:
    return _implementation(equations, ("*", "+", "|"))


if __name__ == "__main__":
    _input = get_input()
    print(f"Day 7 Part 1: {part_1(_input)}")
    print(f"Day 7 Part 2: {part_2(_input)}")
