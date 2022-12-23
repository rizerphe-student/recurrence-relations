"""
Counts n el
"""
from typing import List


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
    while ind < size - 1:
        small = [0] * (ind + 1)
        small.append(1)
        small.extend([0] * (size - ind - 2))
        lst.append(small)
        ind += 1
    cof_lst.reverse()
    lst.append(cof_lst)
    return lst


def multiply_matricies(
    matrix: List[List[float]], subtask: List[List[float]]
) -> List[List[float]]:
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
    return multiply_matricies(
        matrix_to_power(matrix, subtask), matrix_to_power(matrix, power - subtask)
    )


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
            new_value += vector[ind] * element
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
    first_two = [2, 6]
    cof_list = [-7, 18]
    print(n_finder(cof_list, first_two, 4))
