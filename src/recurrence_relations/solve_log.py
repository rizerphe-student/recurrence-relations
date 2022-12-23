"""
Counts n el
"""


def matrix_creator(cof_lst: list[float]) -> list[list[float]]:
    """
    Creates matrix from list of cof
    Args:
        cof_lst (list[float]): list of cofs
    Returns:
        list[list[float]]: result matrix
    """
    size = len(cof_lst)
    lst = []
    ind = 0
    while ind < size - 1:
        small = [0.0] * (ind + 1)
        small.append(1)
        small.extend([0] * (size - ind - 2))
        lst.append(small)
        ind += 1
    cof_lst.reverse()
    lst.append(cof_lst)
    return lst


def multiply_matricies(
    matrix: list[list[float]], subtask: list[list[float]]
) -> list[list[float]]:
    """
    Multiplies two matrixs
    Args:
        matrix (list[list[float]]): first
        subtask (list[list[float]]): second
    Returns:
        list[list[float]]: _description_
    """
    size = len(matrix)
    result = [[0.0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix[i][k] * subtask[k][j]
    return result


def matrix_to_power(matrix: list[list[float]], power: int) -> list[list[float]]:
    """
    Powers matrix to power
    Args:
        matrix (list[list[float]]): matrix
        power (int): power
    Returns:
        list[list[float]]: result
    """
    if power == 1:
        return matrix
    if power == 2:
        return multiply_matricies(matrix, matrix)
    subtask = power // 2
    submatrix = matrix_to_power(matrix_to_power(matrix, subtask), 2)
    return multiply_matricies(submatrix, matrix) if power % 2 else submatrix


def vector_multip(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """
    Args:
        matrix (list[float]): _description_
        vector (list[float]): _description_
    Returns:
        list[float]: _description_
    """
    new_vector = []
    for row in matrix:
        new_value = 0.0
        for ind, element in enumerate(row):
            new_value += vector[ind] * element
        new_vector.append(new_value)
    return new_vector


def n_finder(cof_lst: list[float], el_lst: list[float], number: int) -> float:
    """
    Finds element
    Args:
        cof_list (list[float]): list of cof
        number (int): number to find
    Returns:
        float: number
    """
    if number <= len(el_lst):
        return el_lst[number - 1]
    number -= len(cof_lst)
    matrix = matrix_to_power(matrix_creator(cof_lst), number)
    return vector_multip(matrix, el_lst)[len(cof_lst) - 1]
