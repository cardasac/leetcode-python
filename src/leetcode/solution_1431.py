class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        qualify_max: int = max(candies) - extraCandies

        return [candy >= qualify_max for candy in candies]
