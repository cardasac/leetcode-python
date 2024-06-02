from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude: int = 0
        prev: int = 0

        for number in [0] + gain:
            prev += number
            altitude = max(prev, altitude)

        return altitude
