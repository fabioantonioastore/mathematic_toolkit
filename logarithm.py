from math import log10


def greatest_integer_function(n: int | float) -> int:
    return n // 1


def total_digits(n: int) -> int:
    return greatest_integer_function(log10(n)) + 1
