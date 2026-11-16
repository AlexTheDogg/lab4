"""Проверка существования треугольника и вычисления по трём сторонам.

Аргументы функций — конечные числа int или float.
Вырожденный треугольник (например, 1, 2, 3) считается недопустимым.
"""

import math


def is_valid(a, b, c):
    """Возвращает True, если стороны образуют невырожденный треугольник."""
    return (
        a > 0 and b > 0 and c > 0
        and a + b > c
        and a + c > b
        and b + c > a
    )


def perimeter(a, b, c):
    """Возвращает периметр; для недопустимых сторон вызывает ValueError."""
    if not is_valid(a, b, c):
        raise ValueError("Такие стороны не образуют треугольник")
    return a + b + c


def area(a, b, c):
    """Вычисляет площадь по формуле Герона; неверные стороны — ValueError."""
    if not is_valid(a, b, c):
        raise ValueError("Такие стороны не образуют треугольник")
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))