from solutions.solution_1672 import Solution


def test_maximum_wealth():
    sl = Solution()
    assert sl.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert sl.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert sl.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
