class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        result_div = 0
        result_non_div = 0

        for i in range(1, n + 1):
            if i % m == 0:
                result_div += i
            else:
                result_non_div += i

        return result_non_div - result_div
