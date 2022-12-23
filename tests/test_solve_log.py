"""Test the logarythmic solver."""

import pytest
from hypothesis import given
from hypothesis.strategies import floats, integers, lists
from recurrence_relations import helpers, solve_log


@given(
    lists(
        floats(allow_nan=False, allow_infinity=False, allow_subnormal=False, width=16),
        min_size=2,
        max_size=20,
    ),
    integers(min_value=0, max_value=100),
)
def test_solve_log(values, shift):
    """Test the logarythmic solver."""
    coefficients = values[: len(values) // 2]
    initial_values = values[len(values) // 2 : len(values) // 2 * 2]

    assert solve_log.n_finder(coefficients, initial_values, shift + 1) == pytest.approx(
        helpers.solve_linearly(coefficients, initial_values, shift)[0]
    )
