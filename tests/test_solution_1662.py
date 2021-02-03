from solutions.solution_1662 import Solution


def test_array_strings_are_equal():
    solution = Solution()
    assert solution.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) is True
    assert solution.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False
    assert (
        solution.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])
        is True
    )
