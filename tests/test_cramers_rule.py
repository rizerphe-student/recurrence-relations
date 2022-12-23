"""Test finding a solution to a system of linear equations using Cramer's rule."""
from functools import reduce
from itertools import combinations, starmap
from operator import mul

import pytest
from hypothesis import assume, given
from hypothesis.strategies import floats, lists
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

    for row1, row2 in combinations(coefficients, 2):
        assume(row1 != row2)

        # x + y = 1
        # 2x + 2y = 2
        assume(
            len(
                set(
                    (x / y if y else None)
                    for x, y in zip(row1, row2)
                    if x != 0 or y != 0
                )
            )
            > 1
        )

    # 0x + ay = b
    # 0x + cy = d
    for i in range(3):
        assume(any(coefficients[j][i] for j in range(3)))

    constants = [sum(starmap(mul, zip(row, solutions))) for row in coefficients]
    assert (
        pytest.approx(cramers_rule.cramers_rule(coefficients, constants)) == solutions
    )
