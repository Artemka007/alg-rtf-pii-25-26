from lib import quick_sort


def solution(n, *items):
    if len(items) == 3:
        return items[0] * items[1] * items[2]
    
    items = [i for i in items if i != 0]
    
    if len(items) == 3:
        return items[0] * items[1] * items[2]
    
    quick_sort(items)

    mx = None

    for i in range(-3, 3):
        for j in range(i + 1, 3):
            for k in range(j + 1, 3):
                mult = items[i] * items[j] * items[k]
                if mx is None or mx < mult:
                    mx = mult

    return mx

print(solution(10, -1, 2, 3, -4, -2, 5, -1, 5, -3, -2))