"""Solve a system of linear equations using Cramer's rule.

Determinants are found with expansion by minors
"""


def minor(matrix: list[list[float]], row: int, column: int) -> list[list[float]]:
    """Return the minor of the matrix."""
    return [
        row[:column] + row[column + 1 :] for row in (matrix[:row] + matrix[row + 1 :])
    ]


def determinant(matrix: list[list[float]]) -> float:
    """Return the determinant of the matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(
        (-1) ** i * matrix[0][i] * determinant(minor(matrix, 0, i))
        for i in range(len(matrix))
    )


def replace_column(
    matrix: list[list[float]], column: list[float], index: int
) -> list[list[float]]:
    """Return a copy of the matrix with the specified column replaced."""
    return [
        row[:index] + [column[i]] + row[index + 1 :] for i, row in enumerate(matrix)
    ]


def cramers_rule(
    coefficients: list[list[float]], constants: list[float]
) -> list[float]:
    """Solve a system of linear equations using Cramer's rule

    For the input data:
        coefficients: [
            [a, b, c],
            [d, e, f],
            [g, h, i]
        ]
        constants: [t, u, v]
    Solves the system of equations:
        ax + by + cz = t
        dx + ey + fz = u
        gx + hy + iz = v
    And returns the list:
        [x, y, z]
    """
    det = determinant(coefficients)
    if det == 0:
        raise ValueError("The system has no unique solution.")
    return [
        determinant(replace_column(coefficients, constants, i)) / det
        for i in range(len(coefficients))
    ]
