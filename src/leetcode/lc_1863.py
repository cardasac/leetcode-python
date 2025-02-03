# xor = ((False, True), (True, False))

from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)

    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        result = 0

        for i in powerset(nums):
            inter = 0

            for j in i:
                inter ^= j

            result += inter

        return result

        # bitwise XOR for subsets of array can be solved by performing bitwise
        # OR for every element and final answer multiply by 2 ** len(nums) - 1
        # result = 0
        #
        # for num in nums:
        #     result |= num
        #
        # return result << (len(nums) - 1)
