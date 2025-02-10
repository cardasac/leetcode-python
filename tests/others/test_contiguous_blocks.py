from others.contiguous_blocks import sum_contiguous
import pytest


@pytest.mark.others
@pytest.mark.parametrize(
    "numbers,target,expected",
    [
        ([1, 2, 4, 2, 2, 5, 7], 9, True),
        ([9], 9, True),
        ([1, 2, 3], 9, False),
        ([], 0, False),
        ([], 5, False),
        ([5], 10, False),
        ([-1, -2, -3, -4, -5], -100, False),
        ([-1, 2, -3, 4, -5], 10, False),
        ([1, 2, 3, 4, 5], 9, True),
        ([1, 2, 3, 4, 5], 3, True),
        ([1, 2, 3, 4, 5], 6, True),
        ([1, 2, 3, 4, 5], 1, True),
        ([1, 2, 3], 0, False),
        ([0, 0, 0], 0, True),
    ],
)
def test_sum_contiguous(numbers: list, target: int, expected: bool):
    assert sum_contiguous(numbers, target) is expected
