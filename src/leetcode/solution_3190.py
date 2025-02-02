class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        result = 0

        # for i in nums:
        #     if i % 3 == 0:
        #         continue
        #
        #     if i % 3 != 1:
        #         result += 3 - (i % 3)
        #     else:
        #         result += 1
        for i in nums:
            if i % 3 != 0:
                result += 1

        return result
