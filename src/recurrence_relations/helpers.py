"""Helper functions for testing"""
import itertools
from functools import reduce
from operator import mul


def construct_coefficients(roots: list[float]) -> list[float]:
    """Construct the coefficients of a polynomial given its roots"""
    return [
        sum(reduce(mul, x, (-1) ** i) for x in itertools.combinations(roots, i))
        for i in range(len(roots) + 1)
    ]


def solve_linearly(
    coefficients: list[float], initial: list[float], shift: int
) -> list[float]:
    """Find the values of a linear recurrence relation"""
    if shift == 0:
        return initial
    previous = solve_linearly(coefficients, initial, shift - 1)
    new = [sum(map(mul, coefficients, previous))]
    return previous[1:] + new
