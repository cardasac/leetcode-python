from typing import Literal
from others.contiguous_blocks import sum_contiguous
import pytest


@pytest.mark.others
@pytest.mark.parametrize(
    "numbers,target,expected",
    [
        ([1, 2, 4, 2, 2, 5, 7], 9, True),
        ([9], 9, True),
        ([1, 2, 3], 9, False),
    ],
)
def test_sum_contiguous(numbers: list, target: int, expected: bool):
    assert sum_contiguous(numbers, target) is expected
