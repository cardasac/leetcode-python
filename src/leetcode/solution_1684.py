from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter: int = 0

        for string in words:
            if set(string).issubset(allowed):
                counter += 1

        return counter
