"""
#3 + загальний вигляд
"""


def make_eq(lst_koef, lst_root) -> str:
    """
    makes general equation for recurrent...
    >>> make_eq([-2, 24, 17], [-9, 2, 2])
    -2*(-9)**n + ((24)+(17)*n**1)*(2)**n
    """

    res = "0"
    for i in set(lst_root):
        if lst_root.count(i) > 1:
            res += " + ("
            res += f"({lst_koef[lst_root.index(i)]})"
            for j in range(1, lst_root.count(i)):
                res += f"+({lst_koef[lst_root.index(i)+j]})*n**{j}"
            res += f") * ({i})**n"
        else:
            res += f" + ({lst_koef[lst_root.index(i)]})*({i})**n"
    res = res.replace("0 + ", "")
    return res


def first_n(eqa: str, number: int) -> list:
    """returns the list of n first sequence members"""
    res = []
    i = 0
    while i < number:
        a_n = eval(eqa.replace("n", "i"))
        res.append(a_n)
        i += 1
    return res


first_n(make_eq([3, -2], [-3, -3]), 5)
