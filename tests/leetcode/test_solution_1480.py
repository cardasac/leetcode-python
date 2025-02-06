import pytest
from leetcode.solution_1480 import Solution


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ],
)
def test_runningSum(test_input, expected):
    solution = Solution()
    assert solution.runningSum(test_input) == expected
