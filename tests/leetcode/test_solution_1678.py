from src.leetcode.solution_1678 import Solution


def test_interpret():
    solution = Solution()
    assert solution.interpret("G()(al)") == "Goal"
    assert solution.interpret("G()()()()(al)") == "Gooooal"
    assert solution.interpret("(al)G(al)()()G") == "alGalooG"
