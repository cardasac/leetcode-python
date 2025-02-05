class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result: list[int] = [nums[0]]

        result.extend(
            num + result[index] for index, num in enumerate(nums[1:])
        )
        return result
