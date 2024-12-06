import pytest

from aoc24.day_6 import scan_grid, UP, is_in_bounds, part_1, part_2


@pytest.fixture
def lab_map() -> list[list[str]]:
    return [
        [".", ".", ".",".","#",".",".",".",".","."],
        [".", ".", ".",".",".",".",".",".",".","#"],
        [".", ".", ".",".",".",".",".",".",".","."],
        [".", ".", "#",".",".",".",".",".",".","."],
        [".", ".", ".",".",".",".",".","#",".","."],
        [".", ".", ".",".",".",".",".",".",".","."],
        [".", "#", ".",".","^",".",".",".",".","."],
        [".", ".", ".",".",".",".",".",".","#","."],
        ["#", ".", ".",".",".",".",".",".",".","."],
        [".", ".", ".",".",".",".","#",".",".","."],
    ]


def test_get_initial_position(lab_map):
    position, _, _ = scan_grid(lab_map)
    assert position == (4, 6)


def test_get_initial_heading(lab_map):
    _, heading, _ = scan_grid(lab_map)
    assert heading == UP


def test_get_initial_obstacles(lab_map):
    _, _, obstacles = scan_grid(lab_map)
    assert obstacles == {(4, 0), (9, 1), (2, 3), (7, 4), (1, 6), (8, 7), (0, 8), (6, 9)}


@pytest.mark.parametrize("position,in_bounds", [((0, 0), True), ((-1, 0), False), ((100, 0), False)])
def test_is_in_bounds(position, in_bounds, lab_map):
    assert in_bounds == is_in_bounds(lab_map, position)


def test_part_1(lab_map):
    assert 41 == len(part_1(lab_map))


def test_part_2(lab_map):
    assert 6 == part_2(lab_map, part_1(lab_map))
