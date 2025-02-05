class Solution:
    def getFinalState(
        self,
        nums: list[int],
        k: int,
        multiplier: int,
    ) -> list[int]:
        for num in range(k):
            num = nums.index(min(nums))
            nums[num] *= multiplier

        return nums
