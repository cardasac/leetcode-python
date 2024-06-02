from src.leetcode.lc_3110 import Solution
import pytest


@pytest.mark.parametrize("actual,expected", [("hello", 13), ("zaz", 50)])
def test_array_strings_are_equal(actual, expected):
    assert Solution().scoreOfString(actual) == expected
