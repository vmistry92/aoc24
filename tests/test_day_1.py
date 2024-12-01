import pytest

from aoc24.day_1 import part_1, part_2


@pytest.fixture
def left_list() -> list[int]:
    return sorted([3, 4, 2, 1, 3, 3])


@pytest.fixture
def right_list() -> list[int]:
    return sorted([4, 3, 5, 3, 9, 3])


def test_part_1(left_list, right_list):
    assert part_1(left_list, right_list) == 11


def test_part_2(left_list, right_list):
    assert part_2(left_list, right_list) == 31
