from leetcode.solution_1720 import Solution


def test_decode():
    solution = Solution()
    assert solution.decode([1, 2, 3], 1) == [1, 0, 2, 1]
    assert solution.decode([6, 2, 7, 3], 4) == [4, 2, 0, 7, 4]
