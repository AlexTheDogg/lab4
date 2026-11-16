"""
Запуск из папки проекта:
    python3 -m unittest -v test_geometry
Или:
    python3 test_geometry.py

Требования:
* стороны прямоугольника и квадрата, радиус круга допускают 0, отрицательные значения вызывают ValueError.
* Диагонали допускают ноль, отрицательные стороны вызывают ValueError.
* Треугольник требует положительных сторон и строгих неравенств треугольника.
  is_valid возвращает bool; area/perimeter отклоняют неверные стороны ValueError.

Ожидаемые результаты заданы независимо от вызовов проверяемых функций.
Числовая погрешность: 1e-10 от ожидаемой величины (для нуля — точное сравнение).
Поле actual сохраняет фактический результат для протокола прогона.
"""

import unittest

import circle
import square
import rectangle
import triangle


class CircleTests(unittest.TestCase):

    def test_001_area_integer(self):
        """TC-001: circle.area(5) -> 78.53981633974483."""
        self.actual = circle.area(5)
        expected = 78.53981633974483
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_002_area_zero(self):
        """TC-002: circle.area(0) -> 0."""
        self.actual = circle.area(0)
        self.assertEqual(self.actual, 0)

    def test_003_area_decimal(self):
        """TC-003: circle.area(0.1) -> 0.031415926535897934."""
        self.actual = circle.area(0.1)
        expected = 0.031415926535897934
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_004_perimeter_integer(self):
        """TC-004: circle.perimeter(5) -> 31.41592653589793."""
        self.actual = circle.perimeter(5)
        expected = 31.41592653589793
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_005_perimeter_zero(self):
        """TC-005: circle.perimeter(0) -> 0."""
        self.actual = circle.perimeter(0)
        self.assertEqual(self.actual, 0)

    def test_006_perimeter_decimal(self):
        """TC-006: circle.perimeter(0.1) -> 0.6283185307179586."""
        self.actual = circle.perimeter(0.1)
        expected = 0.6283185307179586
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)


class SquareTests(unittest.TestCase):

    def test_007_area_integer(self):
        """TC-007: square.area(8) -> 64."""
        self.actual = square.area(8)
        expected = 64
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_008_area_zero(self):
        """TC-008: square.area(0) -> 0."""
        self.actual = square.area(0)
        self.assertEqual(self.actual, 0)

    def test_009_area_fraction(self):
        """TC-009: square.area(1.5) -> 2.25."""
        self.actual = square.area(1.5)
        expected = 2.25
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_010_perimeter_integer(self):
        """TC-010: square.perimeter(8) -> 32."""
        self.actual = square.perimeter(8)
        expected = 32
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_011_perimeter_zero(self):
        """TC-011: square.perimeter(0) -> 0."""
        self.actual = square.perimeter(0)
        self.assertEqual(self.actual, 0)

    def test_012_perimeter_fraction(self):
        """TC-012: square.perimeter(1.5) -> 6."""
        self.actual = square.perimeter(1.5)
        expected = 6
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_013_diagonal_integer(self):
        """TC-013: square.diagonal(2) -> 2.8284271247461903."""
        self.actual = square.diagonal(2)
        expected = 2.8284271247461903
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_014_diagonal_zero(self):
        """TC-014: square.diagonal(0) -> 0."""
        self.actual = square.diagonal(0)
        self.assertEqual(self.actual, 0)

    def test_015_diagonal_fraction(self):
        """TC-015: square.diagonal(0.5) -> 0.7071067811865476."""
        self.actual = square.diagonal(0.5)
        expected = 0.7071067811865476
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_016_diagonal_negative(self):
        """TC-016: square.diagonal(-1) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            square.diagonal(-1)
        self.actual = type(caught.exception).__name__


class RectangleTests(unittest.TestCase):

    def test_017_area_integers(self):
        """TC-017: rectangle.area(3, 4) -> 12."""
        self.actual = rectangle.area(3, 4)
        expected = 12
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_018_area_zero_first(self):
        """TC-018: rectangle.area(0, 4) -> 0."""
        self.actual = rectangle.area(0, 4)
        self.assertEqual(self.actual, 0)

    def test_019_area_zero_second(self):
        """TC-019: rectangle.area(4, 0) -> 0."""
        self.actual = rectangle.area(4, 0)
        self.assertEqual(self.actual, 0)

    def test_020_area_fractional(self):
        """TC-020: rectangle.area(1.5, 2.5) -> 3.75."""
        self.actual = rectangle.area(1.5, 2.5)
        expected = 3.75
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_021_perimeter_integers(self):
        """TC-021: rectangle.perimeter(3, 4) -> 14."""
        self.actual = rectangle.perimeter(3, 4)
        expected = 14
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_022_perimeter_zero_first(self):
        """TC-022: rectangle.perimeter(0, 4) -> 8."""
        self.actual = rectangle.perimeter(0, 4)
        expected = 8
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_023_perimeter_both_zero(self):
        """TC-023: rectangle.perimeter(0, 0) -> 0."""
        self.actual = rectangle.perimeter(0, 0)
        self.assertEqual(self.actual, 0)

    def test_024_perimeter_mixed(self):
        """TC-024: rectangle.perimeter(3, 0.5) -> 7."""
        self.actual = rectangle.perimeter(3, 0.5)
        expected = 7
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_025_diagonal_integers(self):
        """TC-025: rectangle.diagonal(3, 4) -> 5."""
        self.actual = rectangle.diagonal(3, 4)
        expected = 5
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_026_diagonal_zero_first(self):
        """TC-026: rectangle.diagonal(0, 4) -> 4."""
        self.actual = rectangle.diagonal(0, 4)
        expected = 4
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_027_diagonal_zero_second(self):
        """TC-027: rectangle.diagonal(4, 0) -> 4."""
        self.actual = rectangle.diagonal(4, 0)
        expected = 4
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_028_diagonal_both_zero(self):
        """TC-028: rectangle.diagonal(0, 0) -> 0."""
        self.actual = rectangle.diagonal(0, 0)
        self.assertEqual(self.actual, 0)

    def test_029_diagonal_fractional(self):
        """TC-029: rectangle.diagonal(0.3, 0.4) -> 0.5."""
        self.actual = rectangle.diagonal(0.3, 0.4)
        expected = 0.5
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_030_diagonal_negative_first(self):
        """TC-030: rectangle.diagonal(-1, 2) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            rectangle.diagonal(-1, 2)
        self.actual = type(caught.exception).__name__

    def test_031_diagonal_negative_second(self):
        """TC-031: rectangle.diagonal(2, -1) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            rectangle.diagonal(2, -1)
        self.actual = type(caught.exception).__name__


class TriangleValidityTests(unittest.TestCase):

    def test_032_right(self):
        """TC-032: triangle.is_valid(3, 4, 5) -> True."""
        self.actual = triangle.is_valid(3, 4, 5)
        self.assertIs(self.actual, True)

    def test_033_near_boundary(self):
        """TC-033: triangle.is_valid(1, 1, 1.999) -> True."""
        self.actual = triangle.is_valid(1, 1, 1.999)
        self.assertIs(self.actual, True)

    def test_034_zero_first(self):
        """TC-034: triangle.is_valid(0, 2, 2) -> False."""
        self.actual = triangle.is_valid(0, 2, 2)
        self.assertIs(self.actual, False)

    def test_035_zero_second(self):
        """TC-035: triangle.is_valid(2, 0, 2) -> False."""
        self.actual = triangle.is_valid(2, 0, 2)
        self.assertIs(self.actual, False)

    def test_036_zero_third(self):
        """TC-036: triangle.is_valid(2, 2, 0) -> False."""
        self.actual = triangle.is_valid(2, 2, 0)
        self.assertIs(self.actual, False)

    def test_037_negative_first(self):
        """TC-037: triangle.is_valid(-1, 2, 2) -> False."""
        self.actual = triangle.is_valid(-1, 2, 2)
        self.assertIs(self.actual, False)

    def test_038_degenerate_third(self):
        """TC-038: triangle.is_valid(1, 2, 3) -> False."""
        self.actual = triangle.is_valid(1, 2, 3)
        self.assertIs(self.actual, False)

    def test_039_degenerate_first(self):
        """TC-039: triangle.is_valid(3, 1, 2) -> False."""
        self.actual = triangle.is_valid(3, 1, 2)
        self.assertIs(self.actual, False)

    def test_040_degenerate_second(self):
        """TC-040: triangle.is_valid(1, 3, 2) -> False."""
        self.actual = triangle.is_valid(1, 3, 2)
        self.assertIs(self.actual, False)

    def test_041_too_long_third(self):
        """TC-041: triangle.is_valid(1, 2, 4) -> False."""
        self.actual = triangle.is_valid(1, 2, 4)
        self.assertIs(self.actual, False)

    def test_042_too_long_first(self):
        """TC-042: triangle.is_valid(4, 1, 2) -> False."""
        self.actual = triangle.is_valid(4, 1, 2)
        self.assertIs(self.actual, False)

    def test_043_too_long_second(self):
        """TC-043: triangle.is_valid(1, 4, 2) -> False."""
        self.actual = triangle.is_valid(1, 4, 2)
        self.assertIs(self.actual, False)

    def test_044_just_outside(self):
        """TC-044: triangle.is_valid(1, 1, 2.001) -> False."""
        self.actual = triangle.is_valid(1, 1, 2.001)
        self.assertIs(self.actual, False)


class TriangleAreaTests(unittest.TestCase):

    def test_045_right(self):
        """TC-045: triangle.area(3, 4, 5) -> 6."""
        self.actual = triangle.area(3, 4, 5)
        expected = 6
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_046_equilateral(self):
        """TC-046: triangle.area(2, 2, 2) -> 1.7320508075688772."""
        self.actual = triangle.area(2, 2, 2)
        expected = 1.7320508075688772
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_047_isosceles(self):
        """TC-047: triangle.area(5, 5, 6) -> 12."""
        self.actual = triangle.area(5, 5, 6)
        expected = 12
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_048_scalene(self):
        """TC-048: triangle.area(4, 5, 6) -> 9.921567416492215."""
        self.actual = triangle.area(4, 5, 6)
        expected = 9.921567416492215
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_049_fractional(self):
        """TC-049: triangle.area(0.3, 0.4, 0.5) -> 0.06."""
        self.actual = triangle.area(0.3, 0.4, 0.5)
        expected = 0.06
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_050_near_boundary(self):
        """TC-050: triangle.area(1, 1, 1.999) -> 0.03160301409576949."""
        self.actual = triangle.area(1, 1, 1.999)
        expected = 0.03160301409576949
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_051_zero_first(self):
        """TC-051: triangle.area(0, 2, 2) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            triangle.area(0, 2, 2)
        self.actual = type(caught.exception).__name__

    def test_052_negative_first(self):
        """TC-052: triangle.area(-1, 2, 2) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            triangle.area(-1, 2, 2)
        self.actual = type(caught.exception).__name__

    def test_053_degenerate_third(self):
        """TC-053: triangle.area(1, 2, 3) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            triangle.area(1, 2, 3)
        self.actual = type(caught.exception).__name__

    def test_054_too_long_third(self):
        """TC-054: triangle.area(1, 2, 4) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            triangle.area(1, 2, 4)
        self.actual = type(caught.exception).__name__


class TrianglePerimeterTests(unittest.TestCase):

    def test_055_right(self):
        """TC-055: triangle.perimeter(3, 4, 5) -> 12."""
        self.actual = triangle.perimeter(3, 4, 5)
        expected = 12
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_056_fractional(self):
        """TC-056: triangle.perimeter(0.3, 0.4, 0.5) -> 1.2."""
        self.actual = triangle.perimeter(0.3, 0.4, 0.5)
        expected = 1.2
        self.assertAlmostEqual(self.actual, expected, delta=abs(expected) * 1e-10)

    def test_057_zero_first(self):
        """TC-057: triangle.perimeter(0, 2, 2) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            triangle.perimeter(0, 2, 2)
        self.actual = type(caught.exception).__name__

    def test_058_negative_first(self):
        """TC-058: triangle.perimeter(-1, 2, 2) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            triangle.perimeter(-1, 2, 2)
        self.actual = type(caught.exception).__name__

    def test_059_degenerate_third(self):
        """TC-059: triangle.perimeter(1, 2, 3) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            triangle.perimeter(1, 2, 3)
        self.actual = type(caught.exception).__name__

    def test_060_too_long_third(self):
        """TC-060: triangle.perimeter(1, 2, 4) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            triangle.perimeter(1, 2, 4)
        self.actual = type(caught.exception).__name__


class NegativeDimensionsTests(unittest.TestCase):

    def test_061_circle_area_negative(self):
        """TC-061: circle.area(-1) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = circle.area(-1)
        self.actual = type(caught.exception).__name__

    def test_062_circle_perimeter_negative(self):
        """TC-062: circle.perimeter(-1) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = circle.perimeter(-1)
        self.actual = type(caught.exception).__name__

    def test_063_square_area_negative(self):
        """TC-063: square.area(-2) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = square.area(-2)
        self.actual = type(caught.exception).__name__

    def test_064_square_perimeter_negative(self):
        """TC-064: square.perimeter(-2) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = square.perimeter(-2)
        self.actual = type(caught.exception).__name__

    def test_065_rectangle_area_negative_first(self):
        """TC-065: rectangle.area(-2, 3) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = rectangle.area(-2, 3)
        self.actual = type(caught.exception).__name__

    def test_066_rectangle_area_negative_second(self):
        """TC-066: rectangle.area(2, -3) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = rectangle.area(2, -3)
        self.actual = type(caught.exception).__name__

    def test_067_rectangle_perimeter_negative_first(self):
        """TC-067: rectangle.perimeter(-2, 3) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = rectangle.perimeter(-2, 3)
        self.actual = type(caught.exception).__name__

    def test_068_rectangle_perimeter_negative_second(self):
        """TC-068: rectangle.perimeter(2, -3) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = rectangle.perimeter(2, -3)
        self.actual = type(caught.exception).__name__


class InvalidTypesTests(unittest.TestCase):

    def test_069_circle_area_bool(self):
        """TC-069: circle.area(True) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = circle.area(True)
        self.actual = type(caught.exception).__name__

    def test_070_circle_perimeter_bool(self):
        """TC-070: circle.perimeter(True) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = circle.perimeter(True)
        self.actual = type(caught.exception).__name__

    def test_071_square_area_bool(self):
        """TC-071: square.area(True) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = square.area(True)
        self.actual = type(caught.exception).__name__

    def test_072_square_perimeter_bool(self):
        """TC-072: square.perimeter(True) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = square.perimeter(True)
        self.actual = type(caught.exception).__name__

    def test_073_square_diagonal_bool(self):
        """TC-073: square.diagonal(True) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = square.diagonal(True)
        self.actual = type(caught.exception).__name__

    def test_074_rectangle_area_bool(self):
        """TC-074: rectangle.area(True, 4) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = rectangle.area(True, 4)
        self.actual = type(caught.exception).__name__

    def test_075_rectangle_perimeter_bool(self):
        """TC-075: rectangle.perimeter(3, True) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = rectangle.perimeter(3, True)
        self.actual = type(caught.exception).__name__

    def test_076_rectangle_diagonal_bool(self):
        """TC-076: rectangle.diagonal(True, 4) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = rectangle.diagonal(True, 4)
        self.actual = type(caught.exception).__name__

    def test_077_triangle_is_valid_bool(self):
        """TC-077: triangle.is_valid(True, 1, 1) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = triangle.is_valid(True, 1, 1)
        self.actual = type(caught.exception).__name__

    def test_078_triangle_area_bool(self):
        """TC-078: triangle.area(1, True, 1) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = triangle.area(1, True, 1)
        self.actual = type(caught.exception).__name__

    def test_079_triangle_perimeter_bool(self):
        """TC-079: triangle.perimeter(1, 1, True) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = triangle.perimeter(1, 1, True)
        self.actual = type(caught.exception).__name__

    def test_080_circle_area_numeric_string(self):
        """TC-080: circle.area('3') -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = circle.area('3')
        self.actual = type(caught.exception).__name__

    def test_081_square_perimeter_numeric_string(self):
        """TC-081: square.perimeter('3') -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = square.perimeter('3')
        self.actual = type(caught.exception).__name__

    def test_082_rectangle_area_none(self):
        """TC-082: rectangle.area(None, 4) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = rectangle.area(None, 4)
        self.actual = type(caught.exception).__name__

    def test_083_rectangle_perimeter_text(self):
        """TC-083: rectangle.perimeter(3, 'abc') -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = rectangle.perimeter(3, 'abc')
        self.actual = type(caught.exception).__name__

    def test_084_triangle_area_list(self):
        """TC-084: triangle.area(3, 4, []) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = triangle.area(3, 4, [])
        self.actual = type(caught.exception).__name__

    def test_085_square_diagonal_empty_string(self):
        """TC-085: square.diagonal('') -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = square.diagonal('')
        self.actual = type(caught.exception).__name__

    def test_086_triangle_perimeter_complex(self):
        """TC-086: triangle.perimeter(3 + 1j, 4, 5) -> TypeError."""
        with self.assertRaises(TypeError) as caught:
            self.actual = triangle.perimeter(3 + 1j, 4, 5)
        self.actual = type(caught.exception).__name__


class NonFiniteValuesTests(unittest.TestCase):

    def test_087_circle_area_nan(self):
        """TC-087: circle.area(float('nan')) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = circle.area(float('nan'))
        self.actual = type(caught.exception).__name__

    def test_088_circle_perimeter_infinity(self):
        """TC-088: circle.perimeter(float('inf')) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = circle.perimeter(float('inf'))
        self.actual = type(caught.exception).__name__

    def test_089_square_diagonal_nan(self):
        """TC-089: square.diagonal(float('nan')) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = square.diagonal(float('nan'))
        self.actual = type(caught.exception).__name__

    def test_090_rectangle_diagonal_infinity(self):
        """TC-090: rectangle.diagonal(3, float('inf')) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = rectangle.diagonal(3, float('inf'))
        self.actual = type(caught.exception).__name__

    def test_091_triangle_is_valid_nan(self):
        """TC-091: triangle.is_valid(float('nan'), 2, 2) -> False."""
        self.actual = triangle.is_valid(float('nan'), 2, 2)
        self.assertIs(self.actual, False)

    def test_092_triangle_perimeter_infinity(self):
        """TC-092: triangle.perimeter(float('inf'), 2, 2) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = triangle.perimeter(float('inf'), 2, 2)
        self.actual = type(caught.exception).__name__

    def test_093_triangle_area_negative_infinity(self):
        """TC-093: triangle.area(2, 2, float('-inf')) -> ValueError."""
        with self.assertRaises(ValueError) as caught:
            self.actual = triangle.area(2, 2, float('-inf'))
        self.actual = type(caught.exception).__name__

if __name__ == "__main__":
    unittest.main(verbosity=2)