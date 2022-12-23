"""Test finding a solution to a system of linear equations using Cramer's rule."""
from functools import reduce
from itertools import combinations, starmap
from operator import mul

import pytest
from hypothesis import assume, given
from hypothesis.strategies import floats, integers, lists
from recurrence_relations import cramers_rule


@given(
    lists(
        floats(min_value=-100, max_value=100, allow_subnormal=False),
        min_size=1,
        max_size=6,
    )
)
def test_determinant_of_diagonal(diagonal: list[float]) -> None:
    """Test that the determinant of a diagonal matrix
    is the product of its diagonal elements."""
    matrix = [[0.0] * len(diagonal) for _ in diagonal]
    for i, element in enumerate(diagonal):
        matrix[i][i] = element
    det = reduce(mul, diagonal)
    assert cramers_rule.determinant(matrix) == pytest.approx(det)


@given(
    lists(
        floats(allow_nan=False, allow_infinity=False, allow_subnormal=False, width=16),
        min_size=9,
        max_size=9,
    ),
    lists(
        floats(allow_nan=False, allow_infinity=False, allow_subnormal=False, width=16),
        min_size=3,
        max_size=3,
    ),
)
def test_cramers_rule(coefficients, solutions):
    """Test finding a solution to a system of linear equations using Cramer's rule."""
    coefficients = [coefficients[i : i + 3] for i in range(0, len(coefficients), 3)]

    # Lazily find whether there is a solution
    assume(cramers_rule.determinant(coefficients))

    constants = [sum(starmap(mul, zip(row, solutions))) for row in coefficients]
    assert (
        pytest.approx(cramers_rule.cramers_rule(coefficients, constants)) == solutions
    )


@given(
    lists(
        floats(allow_nan=False, allow_infinity=False, allow_subnormal=False, width=16),
        min_size=6,
        max_size=6,
    ),
    lists(
        floats(allow_nan=False, allow_infinity=False, allow_subnormal=False, width=16),
        min_size=3,
        max_size=3,
    ),
    integers(0, 1),
    integers(0, 1),
    floats(allow_subnormal=False, allow_infinity=False, allow_nan=False, width=16),
    floats(allow_subnormal=False, allow_infinity=False, allow_nan=False, width=16),
)
def test_cramers_rule_fails(
    coefficients, solutions, index_from, index_to, new_constant, multiple
):
    """Test raising an exception when the solution does not exist"""
    coefficients = [coefficients[i : i + 3] for i in range(0, len(coefficients), 3)]
    constants = [sum(starmap(mul, zip(row, solutions))) for row in coefficients]
    assume(constants[index_from] != new_constant)

    coefficients.insert(index_to, [x * multiple for x in coefficients[index_from]])
    solutions.insert(index_to, new_constant)

    with pytest.raises(ValueError):
        cramers_rule.cramers_rule(coefficients, constants)
