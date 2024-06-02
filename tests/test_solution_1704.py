from src.solution_1704 import Solution


def test_halves_are_alike():
    solution = Solution()

    assert solution.halvesAreAlike("book") is True
    assert solution.halvesAreAlike("textbook") is False
    assert solution.halvesAreAlike("MerryChristmas") is False
    assert solution.halvesAreAlike("AbCdEfGh") is True
