class Solution:
    def numberOfMatches(self, n: int) -> int:
        # total_matches = 0
        #
        # while n != 1:
        #     if n % 2 == 0:
        #         total_matches += n // 2
        #     else:
        #         total_matches += (n - 1) // 2 + 1
        #     n //= 2
        #
        # return total_matches

        def backtracking(n):
            if n == 1:
                return 0

            if n % 2 == 0:
                return n // 2 + backtracking(n // 2)
            else:
                return 1 + n // 2 + backtracking(n // 2)

        return backtracking(n)
