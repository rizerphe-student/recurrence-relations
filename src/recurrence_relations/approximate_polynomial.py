"""Approximate all solutions to a polynomial"""


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
    terms: list[float],
    start: float,
    end: float,
    precision: float,
) -> float | None:
    """Find a solution to a polynomial within a range"""
    if evaluate_polynomial(terms, start) * evaluate_polynomial(terms, end) > 0:
        # If the polynomial has the same sign at both ends, either there is no root
        # or one of the ends is the extremum that's a root
        start_value = evaluate_polynomial(terms, start)
        end_value = evaluate_polynomial(terms, end)

        # If one of the ends of the range is close to zero
        # return the range end that is closer to zero

        # The precision magic was figured out by trial and error
        # and is not guaranteed to work for all cases
        if is_zero(
            start_value, precision ** (1 / 2) * max(abs(start_value), abs(end_value))
        ) or is_zero(
            end_value, precision ** (1 / 2) * max(abs(start_value), abs(end_value))
        ):
            if abs(start_value) < abs(end_value):
                return start
            return end
        # Otherwise, there is no root in the range
        return None
    mid_value = 0.0
    while not (
        is_zero(start - end, precision) and is_zero(mid_value, precision)
    ) and not is_zero(start - end, precision**2):
        start_value = evaluate_polynomial(terms, start)
        mid_value = evaluate_polynomial(terms, (start + end) / 2)
        if start_value * mid_value > 0:
            start = (start + end) / 2
        else:
            end = (start + end) / 2
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

    # Find all ranges that contain a root
    ranges = []
    prev_loc = start
    for extreme in sorted(points_of_interest):
        ranges.append((prev_loc, extreme))
        prev_loc = extreme

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
    return list(sorted(roots))


def approximate_recurrence_polynomial(
    term: list[float], start: float, end: float, precision: float
) -> list[float]:
    """Transforms list"""
    terms = [1.0]
    for elem in term:
        terms.append(-elem)
    return approximate_polynomial(terms, start, end, precision)
