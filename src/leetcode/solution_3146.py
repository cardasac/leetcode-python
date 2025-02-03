class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0

        for (
            i,
            v,
        ) in enumerate(s):
            result += abs(t.index(v) - i)

        return result

        # s_indexes = {char: i for i, char in enumerate(s)}
        # t_indexes = {char: i for i, char in enumerate(t)}
        # count = 0
        #
        # for char in s:
        #     count += abs(s_indexes[char] - t_indexes[char])
        #
        # return count
