from solution_1678 import Solution


def test_interpret():
    solution = Solution()
    assert solution.interpret("G()(al)") == "Goal"
