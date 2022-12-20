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


def remove_duplicates(roots: set[float], precision: float) -> set[float]:
    """Remove duplicate roots"""
    return {round(root, int(math.log10(1 / precision))) for root in roots}


def binary_search(
    terms: list[float], start: float, end: float, precision: float
) -> list[float]:
    """Find all solutions to a polynomial"""
    while not is_zero(start - end, precision):
        sign = evaluate_polynomial(terms, start) * evaluate_polynomial(
            terms, (start + end) / 2
        )
        if sign <= 0:
            end = (start + end) / 2
        else:
            start = (start + end) / 2
    return (start + end) / 2


def approximate_polynomial(
    terms: list[float], start: float, end: float, precision: float
) -> set[float]:
    """Approximate all solutions to a polynomial"""
    # Solve a linear equation
    if len(terms) == 2:
        return {-terms[1] / terms[0]}

    # Find all extremas
    extremas = approximate_polynomial(find_derivative(terms), start, end, precision)
    points_of_interest = extremas.union({start, end})
    print("extremas", terms, extremas)
    print("points_of_interest", terms, points_of_interest)

    # Find all ranges that contain a root
    ranges = []
    sign = evaluate_polynomial(terms, min(points_of_interest))
    prev_loc = start
    for extreme in sorted(points_of_interest):
        new_sign = evaluate_polynomial(terms, extreme)
        if new_sign * sign <= 0:
            ranges.append((prev_loc, extreme))
        sign = new_sign
        prev_loc = extreme
    print("ranges", terms, ranges)

    # Find all roots in each range
    roots = set()
    for start, end in ranges:
        roots.add(binary_search(terms, start, end, precision))
    print("raw roots", terms, roots)
    roots = roots.union(
        {
            extreme
            for extreme in extremas
            if is_zero(evaluate_polynomial(terms, extreme), precision)
        }
    )
    roots = remove_duplicates(roots, precision)
    print("roots", terms, roots)
    return roots


print(approximate_polynomial([1, 0, -1, 0, 0], -100, 100, 0.0001))
# print(
#     approximate_polynomial(
#         [1, 69, -2646, 20820, 130344, -2579424, 12394496, 19568640], -100, 100, 0.0001
#     )
# )

# print(binary_search([3, 0, 0], 0, 100, 0.0001))
