"""The main project file."""

import timeit
from copy import deepcopy
from typing import List

from recurrence_relations.approximate_polynomial import \
    approximate_recurrence_polynomial as approximate_polynomial
from recurrence_relations.cramers_rule import cramers_rule
from recurrence_relations.solve_constant import first_n, make_eq
from recurrence_relations.solve_log import n_finder


def rounder(lst_root: List[float]) -> List[float]:
    """
    Rounds all el in list
    Args:
        lst_root (List[float]): list to round
    Returns:
        List[float]: result
    """
    for ind, ele in enumerate(lst_root):
        lst_root[ind] = round(ele)
    return lst_root


def expression_builder(roots_lst: List[float], coof: int) -> List[List[float]]:
    """
    Counts coof
    Args:
        roots_lst (List[float]): list of roots2
        coof (int): amount of roots
    Returns:
        List[List[float]]: list of roots
    """
    res = []
    fin_res = []
    index = 1
    roots = deepcopy(roots_lst)
    for root in roots:
        amount = roots.count(root)
        sample = f"({root})**n"
        power = 0
        while power < amount:
            res.append(f"{sample} * n**{power}")
            index += 1
            power += 1
        roots.remove(root)
    i = 0
    while i < coof:
        small = []
        for j in res:
            small.append(eval(j.replace("n", "i")))
        fin_res.append(small)
        i += 1
    return fin_res


if __name__ == "__main__":
    values_lst = [2, 9, 29]
    coof_lst = [-7, -16, -12]
    lst_roots = rounder(approximate_polynomial(coof_lst, -100, 100, 0.000001))
    cramers_coof = expression_builder(lst_roots, len(values_lst))
    c_list = cramers_rule(cramers_coof, values_lst)
    print(first_n(make_eq(c_list, lst_roots), 10))
    print(n_finder(coof_lst, values_lst, 1000))
    print(timeit.timeit(lambda: n_finder([-7, -16, -12], [2, 9, 29], 100), number=1))
    print(
        timeit.timeit(
            lambda: first_n(make_eq([73.0, -71.0, -43.0], [-3, -2, -2]), 100), number=1
        )
    )
