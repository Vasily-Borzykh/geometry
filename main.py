from geometry.shapes import Circle, Triangle, calculate_area

circle = Circle(5)
triangle = Triangle(3, 4, 5)

print(f"Площадь круга: {calculate_area(circle)}")
print(f"Площадь треугольника: {calculate_area(triangle)}")
print(f"Треугольник прямоугольный? {triangle.is_right_angled()}")