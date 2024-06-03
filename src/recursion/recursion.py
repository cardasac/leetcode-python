"""Recursion examples."""


def factorial(num: int) -> int:
    return 1 if num == 0 else num * factorial(num - 1)


def fibonacci(num: int) -> int:
    return num if num in {0, 1} else fibonacci(num - 1) + fibonacci(num - 2)
