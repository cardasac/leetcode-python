class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        d = {"++X": 1, "X++": 1, "--X": -1, "X--": -1}

        return sum([d[val] for val in operations])
