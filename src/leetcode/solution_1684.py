from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(set(string).issubset(allowed) for string in words)
