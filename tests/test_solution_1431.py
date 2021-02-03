from solutions.solution_1431 import Solution


def test_kids_with_candies():
    sl = Solution()
    assert sl.kidsWithCandies([2, 3, 5, 1, 3], 3) == [
        True,
        True,
        True,
        False,
        True,
    ]

    assert sl.kidsWithCandies([4, 2, 1, 1, 2], 1) == [
        True,
        False,
        False,
        False,
        False,
    ]

    assert sl.kidsWithCandies([12, 1, 12], 10) == [True, False, True]
