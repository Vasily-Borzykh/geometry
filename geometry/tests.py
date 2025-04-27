import unittest
from shapes import Circle, Triangle, calculate_area
import math

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(calculate_area(circle), math.pi, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0, places=5)

    def test_right_angled_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

    def test_non_right_angled_triangle(self):
        triangle = Triangle(5, 5, 8)
        self.assertFalse(triangle.is_right_angled())

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(0)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_negative_sides(self):
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 3)

if __name__ == "__main__":
    unittest.main()
