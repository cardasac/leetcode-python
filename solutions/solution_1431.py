from typing import List


class Solution:
    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:
        qualify_max: int = max(candies) - extraCandies

        return [candy >= qualify_max for candy in candies]
