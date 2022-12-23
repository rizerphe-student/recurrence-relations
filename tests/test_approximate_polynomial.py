"""Testing module for approximate_polynomial.py"""
import pytest
from hypothesis import assume, given
from hypothesis.strategies import floats, lists
from recurrence_relations import approximate_polynomial, helpers


@given(
    lists(
        floats(
            allow_nan=False,
            allow_infinity=False,
            allow_subnormal=False,
            min_value=-1_000_000,
            max_value=1_000_000,
        ),
        min_size=1,
    ),
    floats(allow_nan=False, allow_infinity=False),
)
def test_derivative(coefficients, constant):
    """Test the derivative function."""
    integral = [
        coefficients[i] / (len(coefficients) - i) for i in range(len(coefficients))
    ] + [constant]
    assert (
        pytest.approx(approximate_polynomial.find_derivative(integral)) == coefficients
    )


@given(
    lists(
        floats(
            allow_nan=False,
            allow_infinity=False,
            allow_subnormal=False,
            width=16
        ),
        min_size=1,
        max_size=8,
    ),
)
def test_approximate_polynomial(roots):
    """Approximate the roots of a polynomial"""
    assume(len(set(roots)) > len(roots) - 2)

    lower_bound = min(roots) - 1
    upper_bound = max(roots) + 1
    bound = max(abs(upper_bound), abs(lower_bound), 1)

    coefficients = helpers.construct_coefficients(roots)
    approximated = approximate_polynomial.approximate_polynomial(
        coefficients, lower_bound, upper_bound, 1e-4
    )
    print(f"Roots: {roots}")
    print(f"Approximated: {approximated}")
    assert pytest.approx(
        approximated,
        abs=bound / 10,
    ) == list(sorted(roots))
