#Рекурентні рівняння

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

    Якщо довжина списку дорівнює 2, то функція повертає множину {-terms[1] / terms[0]}
    В іншому випадку функція :
        шукає екстремуми із похідної : approximate_polynomial(find_derivative(terms), start, end, precision)
    return set[float]