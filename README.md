# Рекурентні рівняння
![Tests](https://github.com/rizerphe/recurrence-relations/actions/workflows/tests.yml/badge.svg)

find_derivative(terms)

    terms: list[float]
    Функція приймає список значень, які є коєфіцієнтами з рухомою крапкою у рівнянні
    Кількість значень - 1  дорівнює найбільшому зі степенів у рівнянні
    Функція обчислює похідну для рівняння
    return list[froat]

evaluate_polynomial(terms, value)

    terms: list[float]
    value: float
    Функція приймає список "terms", який містить коефіцієнти з рухомою крапкою у рівнянні 
    та "value" - число з рухомою крапкою
    Число 'value' підставляється замість 
    Функція повертає розв'язок рівняння(значення функції в точці 'value')

is_zero(value, precision) 

    value: float
    precision: float
    precision - точність
    Функція перевіряє чи близько 'value' до 0
    return True or False

binary_search(terms, start, end, precision)

    terms: list[float]
    start: float
    end: float
    precision: float
    precision - точність
    Функція бінарного пошуку розв'язків рівняння
    return float

approximate_polynomial(terms, start, end, precision)

    terms: list[float]
    start: float
    end: float
    precision: float
    precision - точність

    Шукає приблизні розв'язки рівняння за заданим списком коефіцієнтів та вільним членом,
    (майже завжди) враховуючи повтори коренів.
    Працює з припущенням, що всі корені є в інтерваіл (start, end).
    Для рівняння x^2 + 2x + 3 = 0 список коефіцієнтів має вигляд [1, 2, 3]
