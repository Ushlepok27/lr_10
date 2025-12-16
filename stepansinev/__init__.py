class RectCorrectError(Exception):
    pass

def isCorrectRect(points): # [(-3.4, 1),(9.2, 10)]
    if len(points) != 2 and type(points) == list:
        return False
    
    point1, point2 = points

    if (len(point1) != 2 or len(point2) != 2 or
        not type(point1) == tuple or 
        not type(point2) == tuple or
        not all(isinstance(coord, (int, float)) for coord in point1) or
        not all(isinstance(coord, (int, float)) for coord in point2)):
        return False
    
    x1, y1 = point1
    x2, y2 = point2

    return x1 < x2 and y1 < y2


def isCollisionRect(points1, points2):
    if not isCorrectRect(points1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(points2):
        raise RectCorrectError("2й прямоугольник некоректный")

    if (points1[1][0] <= points2[0][0] or
        points2[1][0] <= points1[0][0] or
        points1[1][1] <= points2[0][1] or
        points2[1][1] <= points1[0][1]):
        return False

    return True


def intersectionAreaRect(points1, points2):
    if not isCorrectRect(points1):
        raise ValueError("1й прямоугольник некоректный")
    if not isCorrectRect(points2):
        raise ValueError("2й прямоугольник некоректный")

    if not isCollisionRect(points1, points2):
        return 0
    
    width = min(points1[1][0], points2[1][0]) - max(points1[0][0], points2[0][0])
    height = min(points1[1][1], points2[1][1]) - max(points1[0][1], points2[0][1])

    return width * height


def intersectionAreaMultiRect(points):
    for i in range(len(points)):
        if not isCorrectRect(points[i]):
            raise RectCorrectError(f"{i}й прямоугольник некоректный")
    
    if not points:
        return 0

    current_rect = points[0]

    for i in range(1, len(points)):
        if not isCollisionRect(current_rect, points[i]):
            return 0
        
        left = max(current_rect[0][0], points[i][0][0])
        bottom = max(current_rect[0][1], points[i][0][1])
        right = min(current_rect[1][0], points[i][1][0])
        top = min(current_rect[1][1], points[i][1][1])
        
        current_rect = [(left, bottom), (right, top)]
    
    width = current_rect[1][0] - current_rect[0][0]
    height = current_rect[1][1] - current_rect[0][1]
    return width * height