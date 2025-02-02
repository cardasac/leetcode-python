from collections import Counter
from heapq import nlargest


class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        # duplicates = {}
        #
        # for item in nums:
        #     if item not in duplicates:
        #         duplicates[item] = 0
        #
        #     duplicates[item] += 1
        #
        # result = {key: val for key, val in duplicates.items() if val > 1}
        #
        # return list(result.keys())
        ctr = Counter(nums)
        return nlargest(2, ctr, key=lambda x: ctr[x])
