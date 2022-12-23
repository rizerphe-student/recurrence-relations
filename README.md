#Рекурентні рівняння

find_derivative(terms)

    terms: list[float]
    Функція приймає список значень, які є коєфіцієнтами з рухомою крапкою у рівнянні
    Кількість значень - 1  дорівнює найбільшому зі степенів у рівнянні
    Функція обчислює похідну для рівняння
    Повертає список коефіцієнтів рівняння похідної
    return list[froat]

evaluate_polynomial(terms, value)

    terms: list[float]
    value: float
    Функція приймає список "terms", який містить коефіцієнти з рухомою крапкою у рівнянні 
    та "value" - число з рухомою крапкою
    Число 'value' підставляється замість 
    Функція повертає розв'язок рівняння(значення функції в точці 'value')
    return froat

is_zero(value, precision) 

    value: float
    precision: float
    precision - точність
    Функція перевіряє чи близько 'value' до 0
    return True or False

binary_search(terms, start, end, precision, max_iter)

    terms: list[float]
    start: float
    end: float
    precision: float
    precision - точність
    max_iter: int = 100
    Функція бінарного пошуку розв'язків рівняння
    return float | None

approximate_polynomial(terms, start, end, precision)

    terms: list[float]
    start: float
    end: float
    precision: float
    precision - точність

    Якщо довжина списку дорівнює 2, то функція повертає множину {-terms[1] / terms[0]}
    В іншому випадку функція :
        шукає екстремуми з похідної : approximate_polynomial(find_derivative(terms), start, end, precision)
        проміжки функції
        корені рівняння
    return list[float]

rounder(lst_root) 

    lst_root: List[float]

    return List[float]

expression_builder(roots_lst: List[float], coof) 
    roots_lst: List[float]
    coof: float

    return str

minor(matrix, row, column)

    matrix: list[list[float]]
    matrix - коефіцієнти біля константи
    row: int
    column: int
    Функція повертає список зі списків розміром row*column,
    у якому row - к-сть списків, а column - к-сть елементів у списках
    return list[list[float]]

determinant(matrix)

    matrix: list[list[float]]
    matrix - коефіцієнти біля константи
    Функція приймає матрицю та рахує її визначник 
    таким способом:

        a b c 
        d e f
        g h i
        M = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    
    return int

replace_column(matrix, column, index)

    matrix: list[list[float]]
    matrix - коефіцієнти біля константи
    column: list[float]
    index: int
    Функція приймає список зі списків(матриця), список елементів для заміни,
    індекс за яким буде відбуватися заміна
    Повертає список зі списків, у яких елементи замінені за індексом
    return list[list[float]]

cramers_rule(coefficients, constants)

    coefficients: list[list[float]]
    coefficients - коефіцієнти біля константи
    constants: list[float]
    constants - елементи послідовності
    Функція  розв'язує систему рівнянь та повертає значення констант
    return list[float]

make_eq(lst_koef, lst_root)
    
    lst_koef: list[float]
    lst_root: list[float]
    Функція підставляє корені рівняння замість "r" та коефіцієнти замість "C"
    Повертає загальний розв'язок рівняння
    return str

first_n(eq, n)

    eq: str
    n: int
    Функція приймає загальний розв'язок рівняння та к-сть членів послідовності
    Повертає n членів послідовності
    return list

matrix_creator(cof_lst) -> 
    cof_lst: List[float]
    cof_lst - список коефіцієнтів
    Функція приймає список коефіцієнтів та 
    повертає список зі списків(матриця), в якому кількість списків дорівнює кількості рядків, а довжина одного списку - кількості стовпців
    return List[List[float]]

multiply_matricies(matrix, subtask)

    matrix: List[List[float]]
    subtask: List[List[float]]
    Функція створює алгоритм множення двох матриць
    Повертає матрицю у вигляді списку зі списків
    return List[List[float]]

matrix_to_power(matrix, power) 
    matrix: List[List[float]]
    power: int
    Функція створює алгоритм піднесення матриці до степеня "power"
    Повертає матрицю у вигляді списку зі списків
    return List[List[float]]

vector_multip(matrix, vector)
    matrix: List[List[float]]
    vector: List[float]
    Функція приймає матрицю у вигляді списку зі списків
    та список чисел, створює алгоритм множення вектора на матрицю
    Повертає список елементів послідовності
    return List[float]

n_finder(cof_lst: List[float], el_lst: List, number: int)
    cof_lst: List[float]
    el_lst: List
    number: int
    Функція приймає список коефіцієнтів, список членів послідовності та число(n-тий член послідовності)
    Повертає n-тий член послідовності
    return float


Під час реалізації даних функцій ми використовували знання з теми рекурентних рівнянь, матриць та чисел Фібоначчі.

Розподіл завдань між командою:

    Богдан Опир - створення алгоритму для знаходження коренів рівняння, створення алгоритму для розв'язку системи лінійних рівнянь

    Богдан Озарко - створення алгоритму (працює за логарифмічний час), який знаходить n-тий член послідовності 

    Анна Монастирська - алгоритм пошуку перших n членів послідовності, пошук загального розв‘язку, створення презентації 

    Юлія Вдовіна -  пошук матеріалів для реалізації 4 пункту, написання звіту

    Тимофій Шевченко - допомога з матрицями

Дана програма дозволяє знайти розв'язки рекурентних рівнянь, перші члени послідовності, достатньо точний n-тий елемент послідовності, загальний розв'язок рівняння. А також порівняти результати двох способів стосовно часу.

Завдання передбачає глибших знань з програмування, вимагає багато зусиль та часу.
