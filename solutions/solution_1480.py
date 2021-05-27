from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result: List[int] = [nums[0]]

        for index, num in enumerate(nums[1:]):
            result.append(num + result[index])

        return result
