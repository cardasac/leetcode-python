from src.leetcode.solution_1688 import Solution


def test_number_of_matches():
    solution = Solution()
    assert solution.numberOfMatches(7) == 6
    assert solution.numberOfMatches(14) == 13
