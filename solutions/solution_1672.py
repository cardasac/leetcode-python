from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # or max([sum(wealth) for wealth in accounts])
        return max(map(sum, accounts))
