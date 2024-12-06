import pytest

from aoc24.day_2 import part_1, part_2


@pytest.fixture
def _input() -> list[list[int]]:
    return [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_part_1(_input):
    assert part_1(_input) == 2


def test_part_2(_input):
    assert part_2(_input) == 4
