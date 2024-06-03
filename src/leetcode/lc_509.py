class Solution:
    def fib(self: "Solution", n: int) -> int:
        return n if n in {0, 1} else self.fib(n - 1) + self.fib(n - 2)

    # def fib(self: "Solution", n: int) -> int:
    #     """Is the iterative approach."""
    #     a, b = 0, 1

    #     for _ in range(n):
    #         a, b = b, a + b

    #     return a
