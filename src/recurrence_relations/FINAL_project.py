"""The main project file"""
import timeit
from copy import deepcopy
from typing import List

from recurrence_relations.approximate_polynomial import approximate_polynomial
from recurrence_relations.cramers_rule import cramers_rule
from recurrence_relations.solve_linear import first_n, make_eq
from recurrence_relations.solve_log import n_finder


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
    print(n_finder(real_lst, values_lst, 10))
    print(
        "#4",
        timeit.timeit(
            stmt="n_finder([-7, -16, -12], [2, 9, 29], 4)",
            setup="from __main__ import n_finder",
        ),
    )
    print(
        "#3",
        timeit.timeit(
            stmt="first_n(make_eq([73.0, -71.0, -43.0], [-3, -2, -2]), 4)",
            setup="from __main__ import first_n, make_eq",
        ),
    )
