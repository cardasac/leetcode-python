class Solution:
    def maximumWealth(self, accounts: list) -> int:
        # or max([sum(wealth) for wealth in accounts])
        return max(map(sum, accounts))
