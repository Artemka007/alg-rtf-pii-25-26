from lib import quick_sort


def solution(n1, n2, *items):
    array1 = []
    array2 = []
    result, i, j, k = 0, 0, 0, 0

    for i in range(n1):
        array1.append(items[i])

    for i in range(n1, n2 + n1):
        array2.append(items[i])
    
    quick_sort(array1)
    quick_sort(array2)
    
    while j < len(array1) and k < len(array2):
        if array1[j] == array2[k]:
            result += 1
            k += 1
            j += 1
            continue
        
        if array1[j] > array2[k]:
            k += 1
            continue
        
        if array1[j] < array2[k]:
            j += 1
            continue
    
    return result


print(solution(5, 5, 1, 1, 2, 2, 3, 0, 1, 3, 3, 4))