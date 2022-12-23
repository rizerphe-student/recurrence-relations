"""Approximate all solutions to a polynomial"""
import math
import timeit
from typing import List
from copy import deepcopy
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

def rounder(lst_root: List[float]) -> List[float]:
    """
    Args:
        lst_root (List[float]): _description_

    Returns:
        List[float]: _description_
    """
    for ind, el in enumerate(lst_root):
        lst_root[ind] = round(el)
    return lst_root

def expression_builder(roots_lst: List[float], coof) -> str:
    res = []
    fin_res = []
    index = 1
    roots = deepcopy(roots_lst)
    for root in roots:
        amount = roots.count(root)
        power = 0
        sample = f"({root})**n"
        for i in range(amount):
            # cof = eval(f"n**{power}")
            res.append(f"{sample} * n**{power}")
            index += 1
            power += 1
        roots.remove(root)
    for n in range(coof):
        small = []
        for j in res:
           small.append(eval(j))
        fin_res.append(small)
    return fin_res

def minor(matrix: list[list[float]], row: int, column: int):
    """Return the minor of the matrix."""
    return [
        row[:column] + row[column + 1 :] for row in (matrix[:row] + matrix[row + 1 :])
    ]

def determinant(matrix: list[list[float]]):
    """Return the determinant of the matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(
        (-1) ** i * matrix[0][i] * determinant(minor(matrix, 0, i))
        for i in range(len(matrix))
    )
def replace_column(matrix: list[list[float]], column: list[float], index: int):
    """Return a copy of the matrix with the specified column replaced."""
    return [
        row[:index] + [column[i]] + row[index + 1 :] for i, row in enumerate(matrix)
    ]
def cramers_rule(coefficients: list[list[float]], constants: list[float]):
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
    d = determinant(coefficients)
    if d == 0:
        raise ValueError("The system has no unique solution.")
    return [
        determinant(replace_column(coefficients, constants, i)) / d
        for i in range(len(coefficients))
    ]

def make_eq(lst_koef, lst_root) -> str:
    """
    makes general equation for recurrent... 
    >>> make_eq([-2, 24, 17], [-9, 2, 2])
    -2*(-9)**n + ((24)+(17)*n**1)*(2)**n
    """

    res = '0'
    for i in set(lst_root):
        if lst_root.count(i) > 1:
            res += f' + ('
            res += f'({lst_koef[lst_root.index(i)]})'
            for j in range(1, lst_root.count(i)):
                res += f'+({lst_koef[lst_root.index(i)+j]})*n**{j}'
            res += f') * ({i})**n'
        else:
            res += f' + ({lst_koef[lst_root.index(i)]})*({i})**n'
    res = res.replace('0 + ', '')
    return res

def first_n(eq: str, n: int) -> list: 
    """returns the list of n first sequence members"""
    res = []
    for i in range(n):
        a_n = eval(eq.replace('n', 'i'))
        res.append(a_n)
    return res

def matrix_creator(cof_lst: List[float]) -> List[List[float]]:
    """
    Creates matrix from list of cof
    Args:
        cof_lst (List[float]): list of cofs
    Returns:
        List[List[float]]: result matrix
    """
    size = len(cof_lst)
    lst = []
    ind = 0
    while ind < size-1:
        small = [0]*(ind+1)
        small.append(1)
        small.extend([0]*(size-ind-2))
        lst.append(small)
        ind += 1
    cof_lst.reverse()
    lst.append(cof_lst)
    return lst

def multiply_matricies(matrix: List[List[float]], subtask: List[List[float]]) -> List[List[float]]:
    """
    Multiplies two matrixs
    Args:
        matrix (List[List[float]]): first
        subtask (List[List[float]]): second
    Returns:
        List[List[float]]: _description_
    """
    size = len(matrix)
    result = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix[i][k] * subtask[k][j]
    return result

def matrix_to_power(matrix: List[List[float]], power: int) -> List[List[float]]:
    """
    Powers matrix to power
    Args:
        matrix (List[List[float]]): matrix
        power (int): power
    Returns:
        List[List[float]]: result
    """
    if power == 1:
        return matrix
    subtask = power // 2
    return multiply_matricies(matrix_to_power(matrix, subtask),\
matrix_to_power(matrix, power - subtask))

def vector_multip(matrix: List[float], vector: List[float]) -> List[float]:
    """
    Args:
        matrix (List[float]): _description_
        vector (List[float]): _description_
    Returns:
        List[float]: _description_
    """
    new_vector = []
    for row in matrix:
        new_value = 0
        ind = 0
        for element in row:
            new_value += vector[ind]*element
            ind += 1
        new_vector.append(new_value)
    return new_vector

def n_finder(cof_lst: List[float], el_lst: List, number: int) -> float:
    """
    Finds element
    Args:
        cof_list (List[float]): list of cof
        number (int): number to find
    Returns:
        float: number
    """
    number -= len(cof_lst)
    matrix = matrix_to_power(matrix_creator(cof_lst), number)
    return vector_multip(matrix, el_lst)[1]

if __name__ == "__main__":
    values_lst = [2, 9, 29]
    a_coof_lst = [1, 7, 16, 12]
    real_lst = [-7, -16, -12]
    lst_root = approximate_polynomial(a_coof_lst, -100, 100, 0.000001)
    lst_root = rounder(lst_root)
    print(lst_root)
    x = expression_builder(lst_root, len(values_lst))
    c_list = cramers_rule(x, values_lst)
    print(c_list)
    print(first_n(make_eq(c_list, lst_root), 10))
    print(n_finder(real_lst, values_lst, 1000))
    timeit.timeit(stmt="n_finder([-7, -16, -12], [2, 9, 29], 8)", setup="from __main__ import n_finder")
    timeit.timeit(stmt="first_n(make_eq([73.0, -71.0, -43.0], [-3, -2, -2]), 8)", setup="from __main__ import first_n")

