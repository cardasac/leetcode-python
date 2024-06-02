from src.leetcode.solution_1732 import Solution


def test_largest_altitude():
    solution = Solution()
    assert solution.largestAltitude([-5, 1, 5, 0, -7]) == 1
    assert solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0
