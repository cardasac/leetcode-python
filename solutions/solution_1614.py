from typing import List


class Solution:
    def maxDepth(self, s: str) -> int:
        nesting_depth: int = 0
        stack: List[str] = []

        # Premature termination can save resources.
        if len(s) < 4:
            return 0

        if s.count("(") == 1:
            return 1

        for char in s:
            if char == "(":
                stack.append("(")

            if char == ")":
                stack.pop()

            nesting_depth = max(nesting_depth, len(stack))

        return nesting_depth
