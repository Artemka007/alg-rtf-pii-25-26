import math
from typing import List, Tuple

from lib import quick_sort


def rotate(o: int, a: int, b: int):
    '''
    Вычисляет векторное произведение векторов OA и OB. 
    Это помогает определить, является ли поворот от точки A к точке 
    B вокруг точки O по часовой стрелке (отрицательное значение) или против (положительное значение).
    '''
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def dist(a: int, b: int):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def graham_scan(N: int, points: List[Tuple[int, int]]):
    n = len(points)
    if n <= 2:
        return points
    
    # Находим опорную точку
    min_idx = 0
    for i in range(1, n):
        if points[i][1] < points[min_idx][1] or \
           (points[i][1] == points[min_idx][1] and points[i][0] > points[min_idx][0]):
            min_idx = i
    pivot = points[min_idx]
    
    # Сортируем по полярному углу
    def polar_angle(p):
        dx = p[0] - pivot[0]
        dy = p[1] - pivot[1]
        return math.atan2(dy, dx), dx*dx + dy*dy
    
    sorted_points = points.copy()
    quick_sort(sorted_points, key=polar_angle)
    
    # Удаляем коллинеарные точки (оставляем самую дальнюю)
    unique_points = [sorted_points[0]]
    for i in range(1, n):
        while i < n - 1 and rotate(pivot, sorted_points[i], sorted_points[i + 1]) == 0:
            i += 1
        unique_points.append(sorted_points[i])
    
    # Строим оболочку
    if len(unique_points) < 3:
        return unique_points
    
    stack = [unique_points[0], unique_points[1], unique_points[2]]
    for i in range(3, len(unique_points)):
        while len(stack) >= 2 and rotate(stack[-2], stack[-1], unique_points[i]) <= 0:
            stack.pop()
        stack.append(unique_points[i])
    
    return stack


def solution(N: int, items: List[int]):
    hull = graham_scan(N, items)
    perimeter = 0.0
    m = len(hull)
    for i in range(m):
        a = hull[i]
        b = hull[(i+1) % m]
        perimeter += dist(a, b)
    
    return "{:.2f}".format(perimeter)

print(solution(5, [(2, 1), (2, 2), (2, 3), (3, 2), (1, 2)]))