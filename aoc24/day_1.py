import os

from functools import lru_cache


@lru_cache
def get_input() -> tuple[list, list]:
    _input = []
    data_file_path = os.path.join(os.path.dirname(__file__), "../data/day_1.txt")
    with open(data_file_path, "r") as fp:
        for line in fp.readlines():
            _input.append(line.replace("\n", "").split("   "))
    
    left_list = sorted([int(i[0]) for i in _input])
    right_list = sorted([int(i[1]) for i in _input])

    return (left_list, right_list)


def part_1(left_list: list[int], right_list: list[int]) -> int:
    answer = 0

    for l, r in zip(left_list, right_list):
        diff = abs(l - r)
        answer += diff

    return answer


def part_2(left_list: list[int], right_list: list[int]) -> int:
    answer = 0

    for l in left_list:
        answer += l * right_list.count(l)

    return answer


if __name__ == "__main__":
    left_list, right_list = get_input()
    print(f"Day 1 Part 1: {part_1(left_list, right_list)}")
    print(f"Day 1 Part 2: {part_2(left_list, right_list)}")
