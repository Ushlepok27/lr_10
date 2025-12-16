import stepansinev


print(f"Корректно ли введены результаты: {stepansinev.isCorrectRect([(-3.4, 1),(9.2, 10)])}")
print(f"Пересекаются ли прямоугольники: {stepansinev.isCollisionRect([(-3.4, 1),(9.2, 10)], [(-3.4, 1),(9.2, 10)])}")
print(f"Площадь пересечения двух прямоугольников: {stepansinev.intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)])}")

rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]

print(f"Уникальная площадь пересечения: {stepansinev.intersectionAreaMultiRect(rectangles)}")