

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        return sum(set(string).issubset(allowed) for string in words)
