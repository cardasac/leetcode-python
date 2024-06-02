from src.leetcode.solution_1684 import Solution


def test_count_consistent_strings():
    solution = Solution()
    assert (
        solution.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]) == 2
    )
    assert (
        solution.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"])
        == 7
    )
    assert (
        solution.countConsistentStrings(
            "cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"],
        )
        == 4
    )
