from lib.quick_sort import quick_sort

def solution(L: int, N: int, points: list[int]) -> int:
    '''
    На прямой располагается 1 ≤ N ≤ 10000 точек с целочисленными координатами –10**9
    ≤ Vi ≤ 10**9. Каждой из точек разрешается сделать ровно одно движение (танцевальное па) в
    любом направлении на расстояние не больше 0 ≤ L ≤ 10**8 и остановиться на другой позиции.
    Какое минимальное количество точек может остаться на прямой после окончания танца
    (все точки после танца, оказывающиеся на одной позиции, сливаются в одну)?
    Args:
        L (int): max distance 0 <= L <= 10**8
        N (int): points count 1 <= M <= 10**5
        points (list[int]): list of points with positions -10**9 <= points[i] <= 10**9
    Returns:
        int: MinimalNumberOfPoints
    '''
    quick_sort(points)

    count = 1

    current_end = points[0] + L

    for i in range(1, N):
        if points[i] >= current_end:
            count += 1
        current_end = points[i] + L
    
    return count


def main():
    import sys
    [L, N] = list(map(int, sys.stdin.readline().split()))
    points = list(map(int, sys.stdin.readline().split()))
    
    result = solution(L, N, points)
    print(result)

if __name__ == "__main__":
    main()