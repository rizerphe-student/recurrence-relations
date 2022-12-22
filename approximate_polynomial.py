"""Approximate all solutions to a polynomial"""
import math


def find_derivative(terms: list[float]) -> list[float]:
    """Find the derivative of a polynomial"""
    return [x * (len(terms) - i - 1) for i, x in enumerate(terms[:-1])]


def evaluate_polynomial(terms: list[float], value: float) -> float:
    """Evaluate a polynomial"""
    return sum(x * value ** (len(terms) - i - 1) for i, x in enumerate(terms))


def is_zero(value: float, precision: float) -> bool:
    """Check if a value is close to zero"""
    return abs(value) < precision


def binary_search(
    terms: list[float], start: float, end: float, precision: float, max_iter: int = 100
) -> float | None:
    """Find all solutions to a polynomial"""
    if is_zero(evaluate_polynomial(terms, start), precision):
        return start
    if is_zero(evaluate_polynomial(terms, end), precision):
        return end
    if evaluate_polynomial(terms, start) * evaluate_polynomial(terms, end) > 0:
        return None
    i = 0
    mid_value = 0.0
    while not (is_zero(start - end, precision) and is_zero(mid_value, precision)):
        start_value = evaluate_polynomial(terms, start)
        mid_value = evaluate_polynomial(terms, (start + end) / 2)
        if start_value * mid_value > 0:
            start = (start + end) / 2
        else:
            end = (start + end) / 2

        i += 1
        if i > max_iter:
            return None
    return (start + end) / 2


def approximate_polynomial(
    terms: list[float], start: float, end: float, precision: float
) -> list[float]:
    """Approximate all solutions to a polynomial"""
    # Solve a linear equation
    if len(terms) == 2:
        return [-terms[1] / terms[0]]

    # Find all extremas
    extremas = approximate_polynomial(find_derivative(terms), start, end, precision)
    points_of_interest = extremas + [start, end]
    print("extremas", terms, extremas)
    print("points_of_interest", terms, points_of_interest)

    # Find all ranges that contain a root
    ranges = []
    sign = evaluate_polynomial(terms, min(points_of_interest))
    prev_loc = start
    for extreme in sorted(points_of_interest):
        new_sign = evaluate_polynomial(terms, extreme)
        ranges.append((prev_loc, extreme))
        prev_loc = extreme
        sign = new_sign
    print("ranges", terms, ranges)

    # Find all roots in each range
    roots = []
    for start_, end_ in ranges:
        if is_zero(start_ - end_, precision) and is_zero(
            evaluate_polynomial(terms, (start_ + end_) / 2), precision
        ):
            roots.append((start_ + end_) / 2)
            continue
        candidate = binary_search(terms, start_, end_, precision)
        if candidate is not None:
            roots.append(candidate)
    print("roots", terms, roots)
    return roots


# print(approximate_polynomial([1, -8, 21, -20, 5], -100, 100, 0.0001))
print(approximate_polynomial([1, 0, -1, 0, 0], -100, 100, 0.000001))
# print(
#     approximate_polynomial(
#         [1, 69, -2646, 20820, 130344, -2579424, 12394496, 19568640], -100, 100, 0.0001
#     )

# print(binary_search([3, 0, 0], 0, 100, 0.0001))
